# -*- coding: utf-8 -*-
# MySQL Workbench Plugin
# Written in MySQL Workbench 6.3.10
#
# Original Author: Hieu Le
# Author: Yao Lei <yaosir.2018@gmail.com>

import time
from wb import *
import grt
import mforms

G = {
    "LAST_CHANGE_DATE": []  # tables last change time; type: int(timestamp)
}

ModuleInfo = DefineModule("ModelDocumentation", author="Yao Lei", version="1.10",
                          description="Generate Markdown documentation from a model")
db_obj = ""

# This plugin takes no arguments
@ModuleInfo.plugin("Netpas", caption="Generate documentation (Markdown)",
                   description="description", input=[wbinputs.currentDiagram()], pluginMenu="Utilities")
@ModuleInfo.export(grt.INT, grt.classes.db_Catalog)
def documentation(diagram):
    global db_obj
    db_obj= [figure for figure in diagram.figures if hasattr(figure, "table")][0].table.owner
    # db name
    title_text = "# {}\n\n".format(db_obj.name)

    body_text = ""
    for figure in diagram.figures:
        if hasattr(figure, "table") and figure.table:
            body_text += writeTableDoc(figure.table)

    # db comment
    title_text += "*{}*\n\n".format(nl2br(db_obj.comment)) if db_obj.comment else "\n\n"

    # db last change date
    last_change_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(max(G["LAST_CHANGE_DATE"])))
    title_text += "{} *{}*\n\n".format("Automatically generate documents. The latest form of document changes by"
                                       , last_change_time)

    # Database Structure
    title_text += "![Database Structure](./{}.db.png)\n\n".format(db_obj.name)

    # merge text
    text = title_text + body_text
    mforms.Utilities.set_clipboard_text(text)
    mforms.App.get().set_status_text("Documentation generated into the clipboard. Paste it to your editor.")

    print("Documentation is copied to the clipboard.")
    return 0

def writeTableDoc(table):
    # table last change date
    last_change_date = time.mktime(time.strptime(table.owner.lastChangeDate, "%Y-%m-%d %H:%M"))
    G["LAST_CHANGE_DATE"].append(int(last_change_date))
    global db_obj
    text = ""
    if db_obj.name == table.owner.name:
        text = "## **<a id='{}'></a>{}**\n\n".format(table.name.lower().replace("_", "-"), table.name.lower())

        text += "---\n\n"

        text += "### *Description:*\n\n"

        text += table.comment + "\n\n"

        text += "### *Columns:*\n\n"

        text += "| Column | Data type | Attributes | Default | Description |\n| --- | --- | --- | --- | ---  |\n"

        for column in table.columns:
            text += writeColumnDoc(column, table)
        text += "\n\n"
        if len(table.indices):
            text += "### *Indices:*\n\n"
            text += "| Name | Columns | Type | Description |\n| --- | --- | --- | --- |\n"

            for index in table.indices:
                text += writeIndexDoc(index)

    text += "\n\n"
    return text

def writeColumnDoc(column, table):
    # column attributes
    attribs = []

    isPrimary = False
    isUnique = False
    for index in table.indices:
        if index.indexType == "PRIMARY":
            for c in index.columns:
                if c.referencedColumn.name == column.name:
                    isPrimary = True
                    break
        if index.indexType == "UNIQUE":
            for c in index.columns:
                if c.referencedColumn.name == column.name:
                    isUnique = True
                    break

    # primary?
    if isPrimary:
        # format label a
        table_name = table.name.lower().replace("_", "-")
        column_name = table.columns[0].name.lower().replace("_", "-")
        # column name
        text = "| <a id='{}-{}'></a>`{}`".format(table_name, column_name, column.name)
    else:
        # column name
        text = "| `{}`".format(column.name)

    # column type name
    if column.simpleType:
        text += " | " + column.simpleType.name
        if 'UNSIGNED' in column.flags:
            text += ' '+ 'UNSIGNED'
        # column max lenght if any
        if column.length != -1:
            text += "(" + str(column.length) + ")"
        if column.characterSetName:
            text +=' ' + 'CHARACTER SET' +' ' +  column.characterSetName
        if column.collationName:
            text +=' ' +  'COLLATE' + ' ' + column.collationName
    else:
        text += " | "

    text += " | "

    # primary?
    if isPrimary:
        attribs.append("PRIMARY")

    # auto increment?
    if column.autoIncrement == 1:
        attribs.append("Auto increments")

    # not null?
    if column.isNotNull == 1:
        attribs.append("Not null")

    # unique?
    if isUnique:
        attribs.append("Unique")

    text += ", ".join(attribs)

    # column default value
    text += " | " + (("`" + column.defaultValue + "`") if column.defaultValue else " ")

    # column description
    text += " | " + (nl2br(column.comment) if column.comment else " ")
    if 'ENUM' in column.formattedType:
        text +='`' +  column.formattedType[4:] + '`'
    if 'SET' in column.formattedType:
        text +='`' + column.formattedType[3:] + '`'
    

    # foreign key
    for fk in table.foreignKeys:
        if fk.columns[0].name == column.name:
            # redirect label a
            fk_filed = fk.referencedColumns[0].name.lower()
            rep_fk_filed = fk.referencedColumns[0].name.lower().replace("_", "-")

            fk_table_name = fk.referencedColumns[0].owner.name.lower()
            rep_fk_table_name = fk.referencedColumns[0].owner.name.lower().replace("_", "-")

            text += ("<br /><br />" if column.comment else "") +"REFERENCES" + "  " + "[**{}**](#{}) ".format(fk_table_name, rep_fk_table_name) + "(" + "[**{}**](#{}-{})".format(fk_filed,fk_table_name,rep_fk_filed) + ")"
            
            if fk.updateRule != 'RESTRICT':
                text += '  ' + 'ON UPDATE' + ' ' + fk.updateRule
            if fk.deleteRule != 'RESTRICT':
                text += '  ' +  'ON DELETE' + ' ' + fk.deleteRule
            break

    # finish
    text += " |" + "\n"
    return text




def writeIndexDoc(index):
    # index name
    text = "| " + index.name

    # index columns
    text += " | " + ", ".join(map(lambda x: "`" + x.referencedColumn.name + "`", index.columns))

    # index type
    text += " | " + index.indexType

    # index description
    text += " | " + (nl2br(index.comment) if index.comment else " ")

    # finish
    text += " |\n"

    return text


def nl2br(text):
    return "<br />".join(map(lambda x: x.strip(), text.split("\n")))

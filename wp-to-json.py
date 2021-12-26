#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Jordi Mas i Hernandez <jmas@softcatala.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.


import json
import xml.etree.ElementTree as ET
import logging
import html2text

def convert(source_filename, target_filename):
    tree = ET.parse(source_filename)
    root = tree.getroot()

    items = []
    words = 0
    for entry in root.iter('item'):
        #print(f"tag: {entry.tag}")
        json_item = {}
        publish = False
        for item in entry:
            #print(item.tag)
        
            if item.tag == "{http://purl.org/rss/1.0/modules/content/}encoded" and item.text is not None:
                # See: https://github.com/Alir3z4/html2text/issues/359
                h = html2text.HTML2Text()
                h.ignore_emphasis = True
                h.body_width = 0
                text = h.handle(item.text)
                json_item['content'] = text
        

            if item.tag == "{http://wordpress.org/export/1.2/}post_id":
                json_item['id'] = item.text

            if item.tag == "{http://wordpress.org/export/1.2/}status":
                if item.text == "publish":
                    publish = True

            if item.tag == "{http://wordpress.org/export/1.2/}post_date":
                json_item['date'] = item.text

            if item.tag == "title":
                json_item['title'] = item.text

            #print(item.tag)
        
        if publish and 'content' in json_item and 'title' in json_item:
            words += len(json_item['content'].split(" "))
            words += len(json_item['title'].split(" "))
            items.append(json_item)
    

    with open(target_filename, 'w') as f:
        json.dump(items, f, indent=4, ensure_ascii=False, sort_keys=True)

    print(f"Exported {len(items)} items with {words} words to {target_filename}")


def main():
    print("Converts a WordPress export to a JSON usable dataset")
    logging.basicConfig(filename="wp-to-json.log", level=logging.DEBUG, filemode="w")
    convert("raw/articles.xml", "dataset/articles.json")
    convert("raw/programes.xml", "dataset/programes.json")

if __name__ == "__main__":
    main()
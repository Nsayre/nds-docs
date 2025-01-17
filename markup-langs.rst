===============
Markdown
===============
Headings

===============
XML
===============

XML stands for eXtensible Markup Language
It was designed to be both human and machine readable

XML is structured in the following way:

<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>

The XML forms a tree that originates at a root element and diverges into child elements.
Elements may contain sub elements, text, or attributes.
Text does not have quotation marks, however attributes must always have them.
The first line is the prolog that defines version and character encoding.
All elements must have a closing tag, and tags are case sensitive.
White space is preserved.

===============
JSON
===============

<?xml version="1.0" encoding="utf8" ?>

<!--
     Stylesheet to transform the swedish electionresult from 2014 to a
     colon separated representation.
     This transforms the files that defines the result for each
     municipiality called slutresultat_<kommunkod>.xml
     The used nodes and their representation is
     VAL/KOMMUN
     K:kommunkod:kommunnamn:antal röster i kommunen
     KRETS_KOMMUN/VALDISTRIKT
     V:valdistriktkod:valdistriktnamn:antal röster i distriktet
     GILTIGA|ÖVRIGA_GILTIGA/GILTIGA
     R:valdistriktkod:partiförkortning:antal röster:röster i procent

     I have preferred to keep this file readable and having
     unneccessary whitespace in the output
-->

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="VAL/KOMMUN">
    <xsl:text>K:</xsl:text>
    <xsl:value-of select="@KOD"/><xsl:text>:</xsl:text>
    <xsl:value-of select="@NAMN"/><xsl:text>:</xsl:text>
    <xsl:value-of select="@RÖSTER"/><xsl:text>
    </xsl:text>

    <xsl:for-each select="KRETS_KOMMUN/VALDISTRIKT">
      <xsl:text>V:</xsl:text>
      <xsl:value-of select="@KOD"/><xsl:text>:</xsl:text>
      <xsl:value-of select="@NAMN"/><xsl:text>:</xsl:text>
      <xsl:value-of select="@RÖSTER"/><xsl:text>
      </xsl:text>
      <xsl:variable name="vdkod"><xsl:value-of select="@KOD"/></xsl:variable>

      <xsl:for-each select="GILTIGA|ÖVRIGA_GILTIGA/GILTIGA">
        <xsl:text>R:</xsl:text>
        <xsl:copy-of select="$vdkod"/><xsl:text>:</xsl:text>
        <xsl:value-of select="@PARTI"/><xsl:text>:</xsl:text>
        <xsl:value-of select="@RÖSTER"/><xsl:text>:</xsl:text>
        <xsl:value-of select="@PROCENT"/><xsl:text>
        </xsl:text>
      </xsl:for-each>
    </xsl:for-each>
  </xsl:template>

</xsl:stylesheet>

<!-- vim: fenc=utf8 sw=2 si sta et -->

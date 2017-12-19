<?xml version="1.0" ?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="LÄN">
    <xsl:for-each select=".">
      <xsl:variable name="lkod" select="@KOD"/>
      <xsl:text>L:</xsl:text>
      <xsl:value-of select="@KOD"/><xsl:text>:</xsl:text>
      <xsl:value-of select="@NAMN"/><xsl:text>
      </xsl:text>

      <xsl:for-each select="KOMMUN">
        <xsl:variable name="kkod" select="@KOD"/>
        <xsl:text>K:</xsl:text><xsl:value-of select="@KOD"/><xsl:text>:</xsl:text>
        <xsl:value-of select="$lkod"/>
        <xsl:value-of select="$kkod"/><xsl:text>:</xsl:text>
        <xsl:value-of select="@NAMN"/><xsl:text>
        </xsl:text>

        <xsl:for-each select="VALDISTRIKT">
          <xsl:variable name="vkod" select="@KOD"/>
          <xsl:text>V:</xsl:text>
          <xsl:value-of select="@KOD"/><xsl:text>:</xsl:text>
          <xsl:value-of select="$lkod"/>
          <xsl:value-of select="$kkod"/>
          <xsl:value-of select="$vkod"/><xsl:text>:</xsl:text>
          <xsl:value-of select="@NAMN"/><xsl:text>
          </xsl:text>

        </xsl:for-each>
      </xsl:for-each>
    </xsl:for-each>
  </xsl:template>
</xsl:stylesheet>

<!-- vim: fenc=utf8 sw=2 si sta et -->

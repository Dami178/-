using NUnit.Framework;
using NUnit.Framework.Legacy;
using System;
using System.Collections.Generic;
using System.Text;

namespace TableParser;

[TestFixture]
public class QuotedFieldTaskTests
{
    [TestCase("''", 0, "", 2)]
    [TestCase("'a'", 0, "a", 3)]
    [TestCase("'a b c'", 0, "a b c", 7)]
    [TestCase(@"some_text ""QF \"""" other_text", 10, "QF \"", 7)]

    [TestCase("\"test\\\\test\"", 0, "test\\test", 12)]

    [TestCase("'abc", 0, "abc", 4)]
    [TestCase("\"hello", 0, "hello", 6)]
    [TestCase("'unclosed string", 0, "unclosed string", 16)]

    [TestCase("abc 'def'", 4, "def", 5)]
    [TestCase("x \"test\" y", 2, "test", 6)]
    [TestCase("start 'middle' end", 6, "middle", 8)]


    [TestCase("\"\"\"\"", 0, "", 2)]

    [TestCase("'  spaces  '", 0, "  spaces  ", 12)]
    [TestCase("\"tab\tchar\"", 0, "tab\tchar", 10)]
    [TestCase("'new\nline'", 0, "new\nline", 10)]

    [TestCase("'привет'", 0, "привет", 8)]

    [TestCase("'!@#$%^&*()'", 0, "!@#$%^&*()", 12)]

    [TestCase("'", 0, "", 1)]
    [TestCase("''", 0, "", 2)]
    [TestCase(@"""gla'", 0, "gla'", 5)]
    [TestCase("'nba", 0, "nba", 4)]
    [TestCase(@"""\\""\\\""", 3, @"\""", 5)]
    [TestCase(@"""axb''pwc""", 0, "axb''pwc", 10)]
    [TestCase(@"""\\\\\""", 0, @"\\""", 7)]
    [TestCase("'b'", 0, "b", 3)]
    [TestCase(@"Zachem ya eto pishu""Kak budto ochenb bespolezo'!""""Luchshe ne stalo ", 19, "Kak budto ochenb bespolezo'!", 30)]


    public void Test(string line, int startIndex, string expectedValue, int expectedLength)
    {
        var actualToken = QuotedFieldTask.ReadQuotedField(line, startIndex);
        ClassicAssert.AreEqual(new Token(expectedValue, startIndex, expectedLength), actualToken);
    }
}

class QuotedFieldTask
{
    public static int GetLength(StringBuilder stringBuild, int startIndex, string line )
    {
        var index = startIndex + 1;
        var firstSymbol = line[startIndex];

        while (index < line.Length)
        {
            if (line[index] == firstSymbol)
                break;
            
            if (line[index] == '\\' && index + 1 < line.Length)
            {
                stringBuild.Append(line[index + 1]);
                index++;
            }

            else
                stringBuild.Append(line[index]);
            
            index++;
        }

        return (index < line.Length) ? index - startIndex + 1 : line.Length - startIndex;
    }

    public static Token ReadQuotedField(string line, int startIndex)
    {
        var stringBuild = new StringBuilder();

        var length = GetLength(stringBuild, startIndex, line);

        return new Token(stringBuild.ToString(), startIndex, length);
    }
}

using NUnit.Framework;
using NUnit.Framework.Legacy;
using System;
using System.Collections.Generic;

namespace Manipulation;

public class TriangleTask
{
    /// <summary>
    /// Возвращает угол (в радианах) между сторонами a и b в треугольнике со сторонами a, b, c 
    /// </summary>
    public static double GetABAngle(double a, double b, double c)
    {
        if (a > 0 && b > 0)
        {
            if (c == 0) return 0;
            if ((!(a >= b + c || b >= a + c || c >= a + b)) && (a > 0))
            {
                var cosA = (a * a + b * b - c * c) / (2 * a * b);

                return Math.Acos(cosA);
            }
        }
        return double.NaN;
    }
}

[TestFixture]
public class TriangleTask_Tests
{
    [TestCase(3, 4, 5, Math.PI / 2)]
    [TestCase(3, 4, 5, Math.PI / 2)]
    [TestCase(1, 1, 2.001, double.NaN)]
    [TestCase(1, 2.001, 1, double.NaN)]
    [TestCase(2.001, 1, 1, double.NaN)]
    [TestCase(0, 5, 5, double.NaN)]
    [TestCase(5, 0, 5, double.NaN)]
    [TestCase(-3, -2, -4, double.NaN)]
    public void TestGetABAngle(double a, double b, double c, double expectedAngle)
    {
        var currRes = TriangleTask.GetABAngle(a, b, c);
        ClassicAssert.AreEqual(currRes, expectedAngle);
    }
}

// See https://aka.ms/new-console-template for more information
using System.Collections.Generic;
/*
En la fábrica de juguetes del Polo Norte, cada juguete tiene un número de identificación único.

Sin embargo, debido a un error en la máquina de juguetes, algunos números se han asignado a más de un juguete.

¡Encuentra el primer número de identificación que se ha repetido, donde la segunda ocurrencia tenga el índice más pequeño!

En otras palabras, si hay más de un número repetido, debes devolver el número cuya segunda ocurrencia aparezca primero en la lista. Si no hay números repetidos, devuelve -1. */


static int findFirstRepeated(int [] arr)
{
    List<int> repeated = new List<int>();
    
    for (int i = 0; i < arr.Length; i++)
    {
        int element = arr[i];
        if (Array.IndexOf(arr, element) != i) 
        {
            repeated.Add(element);
        }
    }

    if (repeated.Count > 0)
    {
        return repeated[0];
    }
    return -1;
}

int[] giftIds = new int[] { 2, 1, 3, 5, 3, 2 };
int[] giftIds2 = new int[] { 1, 2, 3, 4 };
int[] giftIds3 = new int[] { 5, 1, 5, 1 };


Console.WriteLine(findFirstRepeated(giftIds));
Console.WriteLine(findFirstRepeated(giftIds2));
Console.WriteLine(findFirstRepeated(giftIds3));

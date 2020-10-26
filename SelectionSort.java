import java.util.Scanner;  
  
public class SelectionSort
{  
   public static void main(String args[])  
   {  
       int size, i, j, temp;  
       int arr[] = new int[50];  
       Scanner scan = new Scanner(System.in);  
         
       System.out.print(" Array Size");  
       size = scan.nextInt();  
         
       System.out.print(" Array Elements");  
       for(i=0; i<size; i++)  
       {  
           arr[i] = scan.nextInt();  
       }  
         
       System.out.print("Selection Sort");  
       for(i=0; i<size; i++)  
       {  
           for(j=i+1; j<size; j++)  
           {  
               if(arr[i] > arr[j])  
               {  
                   temp = arr[i];  
                   arr[i] = arr[j];  
                   arr[j] = temp;  
               }  
           }  
       }  
         
       System.out.print("Sorted Array");  
       for(i=0; i<size; i++)  
       {  
           System.out.print(arr[i]+ "  ");  
       }  
   }  
}  

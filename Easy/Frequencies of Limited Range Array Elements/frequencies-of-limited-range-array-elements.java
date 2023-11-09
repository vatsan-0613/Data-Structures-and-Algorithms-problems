//{ Driver Code Starts
import java.io.*;
import java.util.*;

class GFG {
    
    public static void main (String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        //testcases
        int t = Integer.parseInt(br.readLine().trim()); 
        while(t-->0){
            
            //size of array
            int N = Integer.parseInt(br.readLine().trim()); 
            int arr[] = new int[N];
            String inputLine[] = br.readLine().trim().split(" ");

            //adding elements to the array
            for(int i = 0 ; i < N; i++){
                arr[i]=Integer.parseInt(inputLine[i]); 
            }
            int P= Integer.parseInt(br.readLine().trim());
            //calling frequncycount() function
            Solution ob = new Solution();
            ob.frequencyCount(arr, N, P); 
            
            //printing array elements
            for(int i = 0; i < N ; i++)
                System.out.print(arr[i] + " " );
            System.out.println();
        }
    }
}




// } Driver Code Ends


class Solution{
    //Function to count the frequency of all elements from 1 to N in the array.
    public static void frequencyCount(int arr[], int N, int P)
    {
        // code here
        int i=0, index;
        
        while(i<N){
            if(arr[i]<0 || arr[i]>N || arr[i]>P){
                i++;
                continue;
            }
            index = arr[i]-1;
            if(arr[index] > 0){
                arr[i] = arr[index];
                arr[index] = -1;
            } else{
                arr[index] -=1;
                arr[i] = 0;
                i++;
            }
        }
        for(i=0; i<N; i++){
            if(arr[i] >=0) arr[i] = 0;
            else arr[i] = -arr[i];
        }
    }
}

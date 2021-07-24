Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>#returns index of x if present in arr, else -1
   def binarysearch(arr,l,r,x):
          #check base case
          if(r>=l):
               mid=l+r-1//2
               #if element is present in the middle
               if arr[mid]==x:
                   return mid
               #if element is smaller than middle number then it will only be present in left half of array
               elif arr[mid]>x:
                   return binarysearch(arr,l,mid-1,x)
               #if element is larger than middle numberthen it will only be present in right half of array
              else:
                   return binarysearch(arr,mid+1,r,x)
          #if reach here then element was not present in given array
          else:
               return -1
    #Driver Code
    arr=[2,3,4,10,40]
    x=10;\n
    binarysearch(arr,0,len(arr)-1,x)

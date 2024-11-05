class Solution:
    def compressedString(self, word: str) -> str:


        n=len(word)
        start=0
        i=1
        cnt=0
        ans=[]
        while i<n:

            while i<n and word[i]==word[i-1] and (i-start)<10:
                i+=1

            if(i-start)==10:
                i-=1
            

            ans.append(str(i-start))
            ans.append(word[start])

            start=i
            i+=1
        
        if start==n-1:

            ans.append(str(i-start))
            ans.append(word[start])





        
        return ''.join(ans)
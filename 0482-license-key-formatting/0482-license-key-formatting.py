class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.replace("-","")
        groups=[]
        if (len(s)%k !=0):
            groups.append(len(s)%k)
        groups+=[k]*(len(s)//k)
        s=s.upper()
        output=[]
        start=0
        for i in groups:
            output.append(s[start:(i+start)])
            start=i+start
        final='-'.join(output)
        return final
                
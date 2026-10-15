class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if k==0 and k==1:
            return s
        no_of_grps=(len(s)//(2*k))+(1 if len(s)%(2*k)!=0 else 0)
        new=[]
        output=[]
        each_grp_size=2*k
        for i in range(no_of_grps):
            for j in s[(each_grp_size)*i:(each_grp_size)*(i+1)]:

                new.append(j)

            new_str="".join(new)
            print(new_str)
            print("test=",new_str[(k-1):0:-1]+new_str[0])
            out_str=new_str[(k-1):0:-1]+new_str[0]+new_str[k:]
            print("out_str",out_str)
            output.append(out_str)
            new=[]
        return ("".join(output))


        
        
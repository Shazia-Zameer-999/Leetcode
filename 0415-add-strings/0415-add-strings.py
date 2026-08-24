class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        length=max(len(num1),len(num2))
        num1=num1.zfill(length)
        num2=num2.zfill(length)

        carry=0
        output=[]
        for index,(i,j) in enumerate(zip(num1[::-1],num2[::-1])):
            print(i,j)
            sum=int(i)+int(j)+carry
            if index==length-1:
                output.append(sum)
            else:
                if sum>9:
                    ones=sum%10
                    carry=1
                    output.append(ones)
                else:
                    carry=0
                    output.append(sum)


        final=output[::-1]
        print(final)
        output=''.join(str(x) for x in final)
        return output                    
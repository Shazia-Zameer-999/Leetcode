class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        if turnedOn>8:
            return []
        H=[h for h in range(12)]
        M=[m for m in range(60)]
        output=[]
        for h in H:
            for m in M:
                #convert h and m to binary and calculate its number of 1s
                h_bin=bin(h).count("1")
                m_bin=bin(m).count("1")
                total=h_bin+m_bin
                if total==turnedOn:
                    if m<10:
                        a=f'{h}:0{m}'
                    else:
                        a=f'{h}:{m}'
                    output.append(a)
        return output
        
        
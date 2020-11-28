numbers = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    14: 'Fourteen',
    15: 'Fifteen',
    16: 'Sixteen',
    17: 'Seventeen',
    18: 'Eighteen',
    19: 'Nineteen',
}
decades = {
    1: 'Ten',
    2: 'Twenty',
    3: 'Thirty',
    4: 'Forty',
    5: 'Fifty',
    6: 'Sixty',
    7: 'Seventy',
    8: 'Eighty',
    9: 'Ninety',
}
modifiers = ['', 'Thousand', 'Million', 'Billion']


class Solution:   
    def getTensAndOnes(self, num: int) -> str:
        if numbers.get(num):
            return numbers.get(num)
        (tens, single) = divmod(num, 10)
        return f"{decades.get(tens, '')} {numbers.get(single, '')}".strip()
    
    def breakNumberIntoTriplets(self, num: int) -> List[str]:
        numAsStr = str(num)
        triplets = []
        i = len(numAsStr)
        while i > 0:
            tempNum = numAsStr[max(i-3, 0):i]
            triplets.append(tempNum)
            i -= 3
        return triplets # triplets will be in reverse order
        
    def getHundredsAndBelow(self, num: int) -> str:
        result = ''
        for n, follow in zip(divmod(num, 100), ("Hundred ", "")):
            if temp := self.getTensAndOnes(n):
                result += f"{temp} {follow}"
        return result.strip()
  
    def parseTriplet(self, num: str, modifier) -> str:
        num = int(num)
        result = numbers.get(num, '') if num < 20 else self.getHundredsAndBelow(num)
        if result != '':
            result += f' {modifier}'
        return result.strip()
    
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        else:
            triplets = self.breakNumberIntoTriplets(num)
            tripletStrings = []
            for modifier, triplet in zip(modifiers, triplets):
                tripletString = self.parseTriplet(triplet, modifier).strip()
                if tripletString:
                    tripletStrings.append(tripletString)
            return ' '.join(tripletStrings[::-1]).strip()

class hello:
    def __init__(self, name, age):
        print(f"my name is {name} and age is {age}")

    def avarage_score(self, m_list: list) -> None:
        try:
            li = []
            for i in m_list:
                if i > 40:
                    li.append(i)

            if len(li) == 0:
                print("No marks above 40!")
                
            av_score = round(sum(li) / len(li))
            sc=print(f"Your score is {av_score}")
            return sc

        except Exception as e:
            print("Something went wrong!", e)


# 🧠 Example
anurag = hello("anurag", 25)
l = [56, 35, 75, 77]
anurag.avarage_score(l)

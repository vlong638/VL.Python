import PrintHelper
PrintHelper.PrintTitle('datetime模块')
PrintHelper.PrintHint('@datetime=datetime.now()')
PrintHelper.PrintHint('@datetime=datetime.datetime(@year,@month,@day,@hour,@minute,@second)')
PrintHelper.PrintHint('@year=@datetime.year')
PrintHelper.PrintHint('@month=@datetime.month')
PrintHelper.PrintHint('@day=@datetime.day')
PrintHelper.PrintHint('@hour=@datetime.hour')
PrintHelper.PrintHint('@minute=@datetime.minute')
PrintHelper.PrintHint('@second=@datetime.second')
PrintHelper.PrintHint('@microsecond=@datetime.microsecond')

import datetime
t1=datetime.datetime.now()
print("t1",t1)
t2=datetime.datetime.now()
print("t2",t2)
print("span",t2-t1)

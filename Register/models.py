from django.db import models

# Create your models here.
# model.pyfrom django.db import models

class User(models.Model):
    '''
    供应商名称、
    联系电话、联系地址、
    电子邮箱、供应商开户行、
    供应商对公账号、企业从业人数、
    每年营业收入、资产总额、
    属于微型企业
    '''
    id = models.AutoField(primary_key=True)     # 创建一个主键
    username = models.CharField(max_length=32)  #  用户名
    password = models.CharField(max_length=32)  # 密码

    # 供应商名称
    SupplierName = models.CharField(max_length=60)
    # 联系电话
    phone = models.CharField(max_length=60)
    # 联系地址
    address = models.CharField(max_length=60)
    # 电子邮箱
    email = models.CharField(max_length=60)
    # 供应商开户行
    SupplierDepositBank = models.CharField(max_length=60)
    # 供应商对公账号
    SupplierCorporateAccountNumber = models.CharField(max_length=60)
    # 企业从业人数
    NumberOfEmployees = models.CharField(max_length=60)
    # 每年营业收入
    AnnualOperatingIncome = models.CharField(max_length=60)
    # 资产总额
    TotalAssets = models.CharField(max_length=60)
    # 属于微型企业
    IsMicroEnterprise = models.BooleanField()
from django.db import models

class Cutoff(models.Model):
    round = models.CharField(max_length=1000, null=True, blank=True)
    category = models.CharField(max_length=100, null = True, blank = True)
    code = models.CharField(max_length=1000, null=True, blank=True)
    college = models.CharField(max_length=1000, null=True, blank=True)
    course = models.CharField(max_length=1000, null=True, blank=True)
    _1G = models.IntegerField(blank=True, null=True)
    _1K = models.IntegerField(blank=True, null=True)
    _1R = models.IntegerField(blank=True, null=True)
    _2AG = models.IntegerField(blank=True, null=True)
    _2AK = models.IntegerField(blank=True, null=True)
    _2AR = models.IntegerField(blank=True, null=True)
    _2BG = models.IntegerField(blank=True, null=True)
    _2BK = models.IntegerField(blank=True, null=True)
    _2BR = models.IntegerField(blank=True, null=True)
    _3AG = models.IntegerField(blank=True, null=True)
    _3AK = models.IntegerField(blank=True, null=True)
    _3AR = models.IntegerField(blank=True, null=True)
    _3BG = models.IntegerField(blank=True, null=True)
    _3BK = models.IntegerField(blank=True, null=True)
    _3BR = models.IntegerField(blank=True, null=True)
    _GM = models.IntegerField(blank=True, null=True)
    _GMK = models.IntegerField(blank=True, null=True)
    _GMP = models.IntegerField(blank=True, null=True)
    _GMR = models.IntegerField(blank=True, null=True)
    _SCG = models.IntegerField(blank=True, null=True)
    _SCK = models.IntegerField(blank=True, null=True)
    _SCR = models.IntegerField(blank=True, null=True)
    _STG = models.IntegerField(blank=True, null=True)
    _STK = models.IntegerField(blank=True, null=True)
    _STR = models.IntegerField(blank=True, null=True)
    H_1G = models.IntegerField(blank=True, null=True)
    H_1K = models.IntegerField(blank=True, null=True)
    H_1R = models.IntegerField(blank=True, null=True)
    H_2AG = models.IntegerField(blank=True, null=True)
    H_2AK = models.IntegerField(blank=True, null=True)
    H_2AR = models.IntegerField(blank=True, null=True)
    H_2BG = models.IntegerField(blank=True, null=True)
    H_2BK = models.IntegerField(blank=True, null=True)
    H_2BR = models.IntegerField(blank=True, null=True)
    H_3AG = models.IntegerField(blank=True, null=True)
    H_3AK = models.IntegerField(blank=True, null=True)
    H_3AR = models.IntegerField(blank=True, null=True)
    H_3BG = models.IntegerField(blank=True, null=True)
    H_3BK = models.IntegerField(blank=True, null=True)
    H_3BR = models.IntegerField(blank=True, null=True)
    H_GM = models.IntegerField(blank=True, null=True)
    H_GMK = models.IntegerField(blank=True, null=True)
    H_GMR = models.IntegerField(blank=True, null=True)
    H_SCG = models.IntegerField(blank=True, null=True)
    H_SCK = models.IntegerField(blank=True, null=True)
    H_SCR = models.IntegerField(blank=True, null=True)
    H_STG = models.IntegerField(blank=True, null=True)
    H_STK = models.IntegerField(blank=True, null=True)
    H_STR = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.college) 





class SeatMatrix(models.Model):
    course_type = models.CharField(max_length=100, null=True, blank = True, verbose_name = 'Course Type')
    district = models.CharField(max_length=100, null=True, blank = True, verbose_name = 'District')
    type = models.CharField(max_length=100, null=True, blank = True, verbose_name = 'Type')
    code = models.CharField(max_length=100, null=True, blank = True, verbose_name = 'Code')
    college_short_name = models.CharField(max_length=100, null=True, blank = True, verbose_name = 'College Short Name')
    college_full_name = models.CharField(max_length=1000, null=True, blank = True, verbose_name = 'College Full Name')
    course_code = models.CharField(max_length=100, null=True, blank = True, verbose_name = 'Course Code')
    _1g = models.IntegerField( null=True, blank = True, verbose_name = '1G')
    _1k = models.IntegerField( null=True, blank = True, verbose_name = '1K')
    _1r = models.IntegerField( null=True, blank = True, verbose_name = '1R')
    _2ag = models.IntegerField( null=True, blank = True, verbose_name = '2AG')
    _2ak = models.IntegerField( null=True, blank = True, verbose_name = '2AK')
    _2ar = models.IntegerField( null=True, blank = True, verbose_name = '2AR')
    _2bg = models.IntegerField( null=True, blank = True, verbose_name = '2BG')
    _2bk = models.IntegerField( null=True, blank = True, verbose_name = '2BK')
    _2br = models.IntegerField( null=True, blank = True, verbose_name = '2BR')
    _3ag = models.IntegerField( null=True, blank = True, verbose_name = '3AG')
    _3ak = models.IntegerField( null=True, blank = True, verbose_name = '3AK')
    _3ar = models.IntegerField( null=True, blank = True, verbose_name = '3AR')
    _3bg = models.IntegerField( null=True, blank = True, verbose_name = '3BG')
    _3bk = models.IntegerField( null=True, blank = True, verbose_name = '3BK')
    _3br = models.IntegerField( null=True, blank = True, verbose_name = '3BR')
    gm = models.IntegerField( null=True, blank = True, verbose_name = 'GM')
    gmk = models.IntegerField( null=True, blank = True, verbose_name = 'GMK')
    gmp = models.IntegerField( null=True, blank = True, verbose_name = 'GMP')
    gmr = models.IntegerField( null=True, blank = True, verbose_name = 'GMR')
    scg = models.IntegerField( null=True, blank = True, verbose_name = 'SCG')
    sck = models.IntegerField( null=True, blank = True, verbose_name = 'SCK')
    scr = models.IntegerField( null=True, blank = True, verbose_name = 'SCR')
    stg = models.IntegerField( null=True, blank = True, verbose_name = 'STG')
    stk = models.IntegerField( null=True, blank = True, verbose_name = 'STK')
    str = models.IntegerField( null=True, blank = True, verbose_name = 'STR')
    total_gen = models.IntegerField( null=True, blank = True, verbose_name = 'Total general reserved seats')
    
    _1h = models.IntegerField( null=True, blank = True, verbose_name = '1H')
    _1kh = models.IntegerField( null=True, blank = True, verbose_name = '1KH')
    _1rh = models.IntegerField( null=True, blank = True, verbose_name = '1RH')
    _2ah = models.IntegerField( null=True, blank = True, verbose_name = '2AH')
    _2akh = models.IntegerField( null=True, blank = True, verbose_name = '2AKH')
    _2arh = models.IntegerField( null=True, blank = True, verbose_name = '2ARH')
    _2bh = models.IntegerField( null=True, blank = True, verbose_name = '2BH')
    _2bkh = models.IntegerField( null=True, blank = True, verbose_name = '2BKH')
    _2brh = models.IntegerField( null=True, blank = True, verbose_name = '2BRH')
    _3ah = models.IntegerField( null=True, blank = True, verbose_name = '3AH')
    _3akh = models.IntegerField( null=True, blank = True, verbose_name = '3AKH')
    _3arh = models.IntegerField( null=True, blank = True, verbose_name = '3ARH')
    _3bh = models.IntegerField( null=True, blank = True, verbose_name = '3BH')
    _3bkh = models.IntegerField( null=True, blank = True, verbose_name = '3BKH')
    _3brh = models.IntegerField( null=True, blank = True, verbose_name = '3BRH')
    gmh = models.IntegerField( null=True, blank = True, verbose_name = 'GMH')
    gmkh = models.IntegerField( null=True, blank = True, verbose_name = 'GMKH')
    gmrh = models.IntegerField( null=True, blank = True, verbose_name = 'GMRH')
    sch = models.IntegerField( null=True, blank = True, verbose_name = 'SCH')
    sckh = models.IntegerField( null=True, blank = True, verbose_name = 'SCKH')
    scrh = models.IntegerField( null=True, blank = True, verbose_name = 'SCRH')
    sth = models.IntegerField( null=True, blank = True, verbose_name = 'STH')
    stkh = models.IntegerField( null=True, blank = True, verbose_name = 'STKH')
    strh = models.IntegerField( null=True, blank = True, verbose_name = 'STRH')
    total_hyd = models.IntegerField( null=True, blank = True, verbose_name = 'Total Hyd Kar Reserved Seats')
    
    agl = models.IntegerField( null=True, blank = True, verbose_name = 'AGL')
    cap = models.IntegerField( null=True, blank = True, verbose_name = 'CAP')
    d = models.IntegerField( null=True, blank = True, verbose_name = 'D')
    dk = models.IntegerField( null=True, blank = True, verbose_name = 'DK')
    jk = models.IntegerField( null=True, blank = True, verbose_name = 'JK')
    ncc = models.IntegerField( null=True, blank = True, verbose_name = 'NCC')
    ph = models.IntegerField( null=True, blank = True, verbose_name = 'PH')
    pv = models.IntegerField( null=True, blank = True, verbose_name = 'PV')
    sg = models.IntegerField( null=True, blank = True, verbose_name = 'S-G')
    spo = models.IntegerField( null=True, blank = True, verbose_name = 'SPO')
    xd = models.IntegerField( null=True, blank = True, verbose_name = 'XD')
    xcp = models.IntegerField( null=True, blank = True, verbose_name = 'XCP')
    total_spl = models.IntegerField( null=True, blank = True, verbose_name = 'Total Special Reserved Seats')
    

    total = models.IntegerField( null=True, blank = True, verbose_name = 'All Total Reserved Seats')
    snq = models.IntegerField( null=True, blank = True, verbose_name = 'SNQ')

    def save(self, *args, **kwargs) -> None:
        if self.college_full_name is None:
            self.college_full_name = self.college_short_name
        return super(SeatMatrix, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return "{} - {}".format(self.college_full_name, self.course_code)






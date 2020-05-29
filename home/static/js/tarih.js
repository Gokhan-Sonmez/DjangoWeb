var mydate=new Date()
var year=mydate.getYear()
if (year < 1000)
year+=1900
var day=mydate.getDay()
var month=mydate.getMonth()
var daym=mydate.getDate()
if (daym<10)
daym="0"+daym
var dayarray=new Array("Pazar","Pazartesi","Sal&#305;","&Ccedil;ar&#351;amba","Persembe","Cuma","Cumartesi")
var montharray=new Array("Ocak","Subat","Mart","Nisan","May&#305;s","Haziran","Temmuz","Agustos","Eylul","Ekim","Kas&#305;m","Aral&#305;k")
document.write(""+daym+" "+montharray[month]+" "+year+"  "+dayarray[day]+"")
/*
     FILE ARCHIVED ON 18:10:10 Dec 13, 2016 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 10:50:16 May 19, 2020.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  LoadShardBlock: 287.153 (3)
  RedisCDXSource: 2.758
  PetaboxLoader3.resolve: 49.692 (2)
  exclusion.robots: 0.193
  CDXLines.iter: 11.632 (3)
  captures_list: 305.361
  esindex: 0.016
  load_resource: 444.699
  exclusion.robots.policy: 0.178
  PetaboxLoader3.datanode: 276.735 (5)
*/
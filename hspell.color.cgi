#!/usr/bin/perl
use CGI;

$query = new CGI;
@keywords = $query->keywords;
$myself = $query->self_url;

my $p = $query->param('text');

sub printDonate() {
  print <<EOF
<form action="https://www.paypal.com/cgi-bin/webscr" method="post">
<input type="hidden" name="cmd" value="_s-xclick">
<input type="hidden" name="hosted_button_id" value="S6R66E99RL6TW">
<input type="image" src="https://www.paypalobjects.com/WEBSCR-640-20110429-1/en_US/i/btn/btn_donate_LG.gif" border="0" name="submit" alt="Send donation via PayPal">
<img alt="" border="0" src="https://www.paypalobjects.com/WEBSCR-640-20110429-1/en_US/i/scr/pixel.gif" width="1" height="1">
</form>
EOF
}



print <<EOF
Content-type: text/html

<HTML DIR=RTL>
<head><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-8-i">
<title>Hspell</title></head>

<STYLE>
.spell {background-color: red; }
</STYLE>
<H1><A HREF=http://hspell.ivrix.org.il/>Hspell</a> - המאיית העברי החופשי</H1>
<H2>טופס הדגמה צבעוני</H2>
כתבו כאן מילים לבדיקה. שגיאות ייצבעו באדום, 
הצעות לתיקון יצוצו עם הזזת הסמן מעל שגיאה.<BR>
<FORM>
<TEXTAREA NAME=text ROWS=10 COLS=60>
$p</TEXTAREA>

<BR>

<INPUT TYPE=SUBMIT VALUE="בדוק!" > 
</FORM>
EOF
;

chdir("/home/danken/.www/cgi-bin/1.1");

$ENV{"PATH"} = $ENV{"PATH"}.':/usr/local/bin';
#$ENV{"LD_LIBRARY_PATH"} = $ENV{"LD_LIBRARY_PATH"}.':/net/cel2-4/local/solaris/lib';

if ($p =~ m/^\s*$/o) {
  print "<HR>\nאזהרה: ייתכן שהטקסט שאתם מקלידים נשמר ומגיע לידי קורא אנושי.<BR>\n";
  print "<P DIR=LTR>\n";
  system("hspell -V");
  print "</P>\n";
  print "<HR>\n";
  print "אם ברצונך להשתמש ב-Hspell באופן מסחרי, או להתייעץ לגבי איות וניתוח מורפולוגי
של עברית באמצעותו, אני פנה/י ל<A HREF=mailto:$com_email>דן
קניגסברג</A>.\n";
  print "<P DIR=LTR>\n";
  print "If you would like to use Hspell comercially, or consult about
Hebrew morphology with Hspell, please contact <A HREF=mailto:$com_email>Dan Kenigsberg</A>.\n";
  print "</P>\n";
  print "</HTML>\n";
  exit(0);
}


print "תוצאות הבדיקה:<br>\n";

print "<PRE>\n";

my $res = open(HSPELL, "| ./color.pl ");
print HSPELL "$p\n";
close(HSPELL);
print "</PRE>\n";

print <<EOF
<BR><HR>
אם מצאתם שגיאה, או גיליתם מילה שחסרה במילון של Hspell, או לכל הערה אחרת,
אתם מוזמנים לפנות ל<a href=mailto:$tech_email>רשימת הדיוור</a>.
אם ברצונכם לתרום מילה ל&#1470;<LRM>Hspell, אנא וודאו מהו האיות הנכון שלה בכתיב
חסר&#1470;הניקוד ע\"פ כללי האקדמיה ללשון העברית, תוך הסתייעות במילון החביב
עליכם.
EOF
;
printDonate();

print <<EOF
</HTML>
EOF
;


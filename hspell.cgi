#!/usr/bin/perl
use CGI;

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


$query = new CGI;
@keywords = $query->keywords;
$myself = $query->self_url;

my $p = $query->param('text');
my $ling = $query->param('ling') eq "on" ? "checked" : "";
my $corr = $query->param('corr') eq "on" ? "checked" : "";
my $inquis_he = $query->param('inquis_he') eq "on" ? "checked" : "";

print <<EOF
Content-type: text/html

<head><meta http-equiv="Content-Type" content="text/html; charset=iso-8859-8-i">
<title>Hspell - Free Hebrew Spell-Checker</title></head>

<HTML DIR=RTL>
<H1><A HREF=http://ivrix.org.il/projects/spell-checker/>Hspell</a> - המאיית העברי החופשי</H1><H2>טופס הדגמה</H2>
עמוד זה מדגים את פעולת Hspell למי שאין ביכולתו/ברצונו להתקין אותה.<BR>
אם אתם כאן כדי לבדוק טקסט שלכם, ומעוניינים פחות לבחון את התכונות המופלאות של
Hspell, אתם מוזמנים לבדוק את 
<A HREF=hspell.color.cgi>טופס ההדגמה הצבעוני</A>.<BR>
שימו לב, שהעמוד לא הכי זריז בעולם (במיוחד אם מבקשים מידע לשוני).<BR><BR>

כתבו כאן מילים לבדיקה:<BR>

<FORM>
<TEXTAREA NAME=text ROWS=4 COLS=40>
$p</TEXTAREA>

<INPUT TYPE=CHECKBOX NAME="ling" $ling>
<LABEL for="ling">עם מידע לשוני</LABEL>
<INPUT TYPE=CHECKBOX NAME="corr" $corr>
<LABEL for="corr">הצעות לתיקון</LABEL>
<INPUT TYPE=CHECKBOX NAME="inquis_he" $inquis_he>
<LABEL for="inquis_he">ה"א השאלה</LABEL>
<BR>

<INPUT TYPE=SUBMIT VALUE="בדוק!" > 
</FORM>
EOF
;

#print $query->param,"<br>\n";
chdir("/home/danken/.www/cgi-bin/1.1");

$ENV{"PATH"} = $ENV{"PATH"}.':/usr/local/bin';
#$ENV{"LD_LIBRARY_PATH"} = $ENV{"LD_LIBRARY_PATH"}.':/net/cel2-4/local/solaris/lib';
#print "PATH is ".$ENV{'PATH'}."\n";
#print "LD_LIBRARY_PATH is ".$ENV{'LD_LIBRARY_PATH'}."\n";

if ($p =~ m/^\s*$/o) {
  print "<HR>\nאזהרה: ייתכן שהטקסט שאתם מקלידים נשמר ומגיע לידי קורא אנושי.<BR>\n";
  print "<P DIR=LTR>\n";
  my $res = system("hspell -V");
  print "</P>\n";
#print "res is $res. exclam is $!\n";
  print "<HR>\n";
  print "אם ברצונך להשתמש ב-Hspell באופן מסחרי, או להתייעץ לגבי איות וניתוח מורפולוגי
של עברית באמצעותו, אנא פנה/י ל<A HREF=mailto:danken\@gmail.com>דן
קניגסברג</A>.\nנשמח לקבל פניות בנושאים טכניים גם ב<A HREF=mailto:hspell-devel\@lists.sourceforge.net>רשימת הדיוור</A>.\n";
  print "<P DIR=LTR>\n";
  print "If you would like to use Hspell comercially, or consult about
Hebrew morphology with Hspell, please contact <A HREF=mailto:danken\@gmail.com>Dan Kenigsberg</A>.\n";
  print "</P>\n";
  printDonate();
  print "</HTML>\n";
  exit(0);
}


print "תוצאות הבדיקה של \"$p\":<br>\n";
#print "<P><A HREF=$keywords[0]>".join(' ',@keywords)."</A><BR>\n";

my $hspell_param="";
$hspell_param.=" -l" if($ling);
$hspell_param.=" -c" if($corr);
$hspell_param.=" -H" if($inquis_he);

print "<PRE>\n";

my $res = open(HSPELL, "| hspell $hspell_param");
print HSPELL "$p\n";
close(HSPELL);
#print "hspell returned $?\n";

print "</PRE>\n";
#print "res is $res\n";

print "<BR><HR>\n";
print "אם מצאתם שגיאה, או גיליתם מילה שחסרה במילון של Hspell, או לכל הערה אחרת,
אתם מוזמנים לפנות לדן קניגסברג בדואל
<a href=mailto:danken\@gmail.com>danken\@gmail.com</a>.\n";
print "אם ברצונכם לתרום מילה ל&#1470;<LRM>Hspell, אנא וודאו מהו האיות הנכון שלה בכתיב
חסר&#1470;הניקוד ע\"פ כללי האקדמיה ללשון העברית, תוך הסתייעות במילון החביב עליכם.\n";
printDonate();
print "</HTML>\n";


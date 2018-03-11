#!/usr/bin/perl

use IPC::Open2;

open2(\*RDRFH, \*WTRFH, "hspell -a");

#read the speller signature line
$_ = <RDRFH>;

while (<>) {
        chomp;
	@array = split(/([^à-ú'"]+)/o);
        foreach $word (@array) {
                if ($word =~ m/[à-ú'"]/o) {
                        print WTRFH "$word\n";
                        my $r = <RDRFH>;
                        my $sugg="";
                        if ($r =~ m/&.*: (.*)/) {
                                $sugg = " title=\"$1\"";
                        }
                        if ($r !~ m/^\*/) {
                                $word = "<SPAN CLASS=spell$sugg>$word</SPAN>";
                        }
                        $r = <RDRFH>;
                }
                print "$word";
        }
        print "\n";
}


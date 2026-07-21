# Ohbot text to speech on Windows

ohbot.setSynthesizer(synth,ID = "",region ='westeurope')
----------

| synth | Full Name |
|----|-------- |
| “sapi” | SAPI4 speech |
| “sapi5” | SAPI5 speech |
| “espeak-ng” | espeak-ng speech |
| “espeak” | espeak speech |
| “Azure” | Microsoft web based text to speech |

If you have an Azure account you can use:

use ohbot.setSynthesizer("Azure", "<key>", "<region>") 
where <key> and <region> come from your Azure acccount

You can set up a free Azure account here:

<a href="https://azure.microsoft.com/en-gb/free/" target="_blank"></a>

For Example:
```python
ohbot.setSynthesizer("espeak")
```

Note that the SAPI speech uses SAPI4 voices. 

In Windows 10 you can see the available SAPI4 voices in Control Panel:Text to Speech.   

In Windows 11 you can get a list of these voices by looking for Text to Speech setttings or in PowerShell by running this script:

Add-Type -AssemblyName System.Speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$synth.GetInstalledVoices() | ForEach-Object {
    $_.VoiceInfo
}

Use SAPI5 for SAPI5 voices.  You can see available voices through the speech settings in Windows 10 and Windows 11.  To get extra voices select Add Voices through the Time & Language : Speech settings in Windows 11 or install language packs with speech capability in Windows 10. 

To use SAPI5 you need to install some extra libraries.  In command shell run this.  Note that this is for Python 3.13 - please adjust it if you are using a different version of Python:

py -3.13 -m pip install winrt-Windows.Foundation winrt-Windows.Foundation.Collections winrt-Windows.Media.SpeechSynthesis winrt-Windows.Storage.Streams

Use ohbot.setVoice() to set the voice depending on the synthesizer:

<b>Using Azure voices</b>

ohbot.setVoice(voice, language = "en-GB", gender = 'Female')

language and gender are only supported by Azure, SAPI and SAPI5 voices.  
Gender is overridden by any selected voice.  
If you leave voice blank and define language and gender then the first voice in this language with this gender will be used

<b>Using SAPI or SAPI5</b>

The voice can contain any of the following arguments:

| Name| Description|
| --- |------|
| -a0 to -a100   | amplitude |
| -r-10 to r10   | rate |
| -p-10 to p10   | pitch (SAPI5 only) |
| -v any part of the name of a SAPI voice (eg. -vHazel or -vZira) | voice |

For Example:
```python
ohbot.setVoice("-a82 -r12 -vzira")

```

<b>Using ESPEAK</b>

http://espeak.sourceforge.net/commands.html<br>

| Name| Description|
| --- |------|
| -v followed by a letter code|look in program files\espeak\espeak-data\voices to see what's available|
|   +m1 to m7   | male voices |
|   +f1 to f4   | remale voices |
|   +croak or whisper   | tone |
|   -a0 to a200   | amplitude |
|   -s80 to s500   | speed |
|   -p0 to p99   | pitch |


Examples:<br>

| Command | Result |
| ------ | ------- |
| ``ohbot.setVoice("-ven+croak")`` | English croaky voice |
| ``ohbot.setVoice("-vzh+m2 -s26")`` | Chinese male voice, Fast |
| ``ohbot.setVoice("-vfr+f1 -p99 -s180")`` | French female whisper voice, medium speed and high pitched |

More examples can be found in our [voices example program.](https://github.com/ohbot/ohbot-python/blob/master/examples/Windows/changingVoices.py)

<b>Using ESPEAK-NG</b>

Supports some of the ESPEAK parameters but some are missing.




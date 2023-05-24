; �ýű�ʹ�� HM VNISEdit �ű��༭���򵼲���

; ��װ�����ʼ���峣��
!define PRODUCT_NAME "CreditCheck"
!define PRODUCT_VERSION "0.2.0"
!define PRODUCT_PUBLISHER "Jiayi Yang"
!define PRODUCT_WEB_SITE "https://gitee.com/yangjywhu/CreditCheck"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"
!define PRODUCT_STARTMENU_REGVAL "NSIS:StartMenuDir"

SetCompressor lzma

; ------ MUI �ִ����涨�� (1.67 �汾���ϼ���) ------
!include "MUI.nsh"

; MUI Ԥ���峣��
!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"

; ��ӭҳ��
!insertmacro MUI_PAGE_WELCOME
; ��װĿ¼ѡ��ҳ��
!insertmacro MUI_PAGE_DIRECTORY
; ��ʼ�˵�����ҳ��
var ICONS_GROUP
!define MUI_STARTMENUPAGE_NODISABLE
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "CreditCheck"
!define MUI_STARTMENUPAGE_REGISTRY_ROOT "${PRODUCT_UNINST_ROOT_KEY}"
!define MUI_STARTMENUPAGE_REGISTRY_KEY "${PRODUCT_UNINST_KEY}"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "${PRODUCT_STARTMENU_REGVAL}"
!insertmacro MUI_PAGE_STARTMENU Application $ICONS_GROUP
; ��װ����ҳ��
!insertmacro MUI_PAGE_INSTFILES
; ��װ���ҳ��
!insertmacro MUI_PAGE_FINISH

; ��װж�ع���ҳ��
!insertmacro MUI_UNPAGE_INSTFILES

; ��װ�����������������
!insertmacro MUI_LANGUAGE "SimpChinese"

; ��װԤ�ͷ��ļ�
!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS
; ------ MUI �ִ����涨����� ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "CreditCheck.exe"
InstallDir "$PROGRAMFILES\CreditCheck"
ShowInstDetails show
ShowUnInstDetails show

Section "MainSection" SEC01
  SetOutPath "$INSTDIR"
  SetOverwrite ifnewer
  File /r "dist\main\*.*"

; ������ʼ�˵���ݷ�ʽ
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
  CreateShortCut "$DESKTOP\ѧ����鹤��.lnk" "$INSTDIR\main.exe"
  !insertmacro MUI_STARTMENU_WRITE_END
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd

/******************************
 *  �����ǰ�װ�����ж�ز���  *
 ******************************/

Section Uninstall
  !insertmacro MUI_STARTMENU_GETFOLDER "Application" $ICONS_GROUP

  Delete "$DESKTOP\ѧ����鹤��.lnk"

  RMDir /r "$INSTDIR\shiboken6"
  RMDir /r "$INSTDIR\setuptools-65.5.0.dist-info"
  RMDir /r "$INSTDIR\PySide6"
  RMDir /r "$INSTDIR\PIL"
  RMDir /r "$INSTDIR\pdfminer"
  RMDir /r "$INSTDIR\markupsafe"
  RMDir /r "$INSTDIR\lxml"
  RMDir /r "$INSTDIR\docx"
  RMDir /r "$INSTDIR\doc"
  RMDir /r "$INSTDIR\cryptography-40.0.2.dist-info"
  RMDir /r "$INSTDIR\cryptography"
  RMDir /r "$INSTDIR\charset_normalizer"
  Delete "$INSTDIR\VCRUNTIME140.dll"
  Delete "$INSTDIR\VCRUNTIME140_1.dll"
  Delete "$INSTDIR\base_library.zip"
  Delete "$INSTDIR\_asyncio.pyd"
  Delete "$INSTDIR\_bz2.pyd"
  Delete "$INSTDIR\_cffi_backend.cp311-win_amd64.pyd"
  Delete "$INSTDIR\_ctypes.pyd"
  Delete "$INSTDIR\_decimal.pyd"
  Delete "$INSTDIR\_elementtree.pyd"
  Delete "$INSTDIR\_hashlib.pyd"
  Delete "$INSTDIR\_lzma.pyd"
  Delete "$INSTDIR\_multiprocessing.pyd"
  Delete "$INSTDIR\_overlapped.pyd"
  Delete "$INSTDIR\_queue.pyd"
  Delete "$INSTDIR\_socket.pyd"
  Delete "$INSTDIR\_ssl.pyd"
  Delete "$INSTDIR\_zoneinfo.pyd"
  Delete "$INSTDIR\base_library.zi"
  Delete "$INSTDIR\libcrypto-1_1.dll"
  Delete "$INSTDIR\libffi-8.dll"
  Delete "$INSTDIR\libssl-1_1.dll"
  Delete "$INSTDIR\main.exe"
  Delete "$INSTDIR\pyexpat.pyd"
  Delete "$INSTDIR\python3.dll"
  Delete "$INSTDIR\python311.dll"
  Delete "$INSTDIR\select.pyd"
  Delete "$INSTDIR\unicodedata.pyd"

  Delete "$INSTDIR\uninst.exe"

  RMDir "$INSTDIR"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  SetAutoClose true
SectionEnd

#-- ���� NSIS �ű��༭�������� Function ���α�������� Section ����֮���д���Ա��ⰲװ�������δ��Ԥ֪�����⡣--#

Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "��ȷʵҪ��ȫ�Ƴ� $(^Name) ���������е������" IDYES +2
  Abort
FunctionEnd

Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) �ѳɹ��ش����ļ�����Ƴ���"
FunctionEnd

%define rname lxx74

Summary:	A Linux Printer Driver for Lexmark X74 All In One
Name:		cups-drivers-%{rname}
Version:	0.8.4.2
Release:	%mkrel 11
License:	GPL
Group:		System/Printing
URL:		http://home.online.no/~enrio/
Source0:	http://home.online.no/~enrio/%{rname}-cups-%{version}.tar.gz
Requires:	cups
BuildRequires:	cups-devel
BuildRequires:	cups
Conflicts:	cups-drivers = 2007
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A Linux Printer Driver for Lexmark X74 All In One

The driver also works with:
 o Lexmark X75

The driver also should work with:
 o Compaq  - IJ670 Series, Inkjet Printer
 o Lexmark - Inkjet 4104, Inkjet Printer, Lexmark X76, Lexmark Z13,
             Lexmark Z14, Lexmark Z23-Z33, Lexmark Z24-Z34, Lexmark Z25-Z35
 o Samsung - MJC-940_2200_530, MJC-950_2130_530

This package contains CUPS drivers (PPD) for the following printers:

 o Compaq IJ670
 o Compaq Inkjet Printer
 o Lexmark All In One
 o Lexmark Inkjet Printer
 o Lexmark X74
 o Lexmark X75
 o Lexmark X76
 o Lexmark Z13
 o Lexmark Z14
 o Lexmark Z23
 o Lexmark Z24
 o Lexmark Z25
 o Lexmark Z33
 o Lexmark Z34
 o Lexmark Z35
 o Samsung MJC-2130
 o Samsung MJC-2200
 o Samsung MJC-530
 o Samsung MJC-940
 o Samsung MJC-950
 o Lexmark All In One

%prep

%setup -q -n %{rname}-cups-%{version}

%build
perl -p -i -e "s|gcc|gcc %{optflags} %{ldflags}|g" Makefile
make clean
%make

gunzip lxx74.ppd.gz
cp lxx74.ppd Compaq-IJ670-lxx74.ppd
perl -p -i -e 's/All In One/IJ670/gi' Compaq-IJ670-lxx74.ppd
cp lxx74.ppd Compaq-Inkjet_Printer-lxx74.ppd
perl -p -i -e 's/All In One/Inkjet Printer/gi' Compaq-Inkjet_Printer-lxx74.ppd
perl -p -i -e 's/Lexmark/Compaq/gi' Compaq-*-lxx74.ppd
cp lxx74.ppd Lexmark-X74-lxx74.ppd
perl -p -i -e 's/All In One/X74/gi' Lexmark-X74-lxx74.ppd
cp lxx74.ppd Lexmark-X75-lxx74.ppd
perl -p -i -e 's/All In One/X75/gi' Lexmark-X75-lxx74.ppd
cp lxx74.ppd Lexmark-X76-lxx74.ppd
perl -p -i -e 's/All In One/X76/gi' Lexmark-X76-lxx74.ppd
cp lxx74.ppd Lexmark-Z13-lxx74.ppd
perl -p -i -e 's/All In One/Z13/gi' Lexmark-Z13-lxx74.ppd
cp lxx74.ppd Lexmark-Z14-lxx74.ppd
perl -p -i -e 's/All In One/Z14/gi' Lexmark-Z14-lxx74.ppd
cp lxx74.ppd Lexmark-Z23-lxx74.ppd
perl -p -i -e 's/All In One/Z23/gi' Lexmark-Z23-lxx74.ppd
cp lxx74.ppd Lexmark-Z33-lxx74.ppd
perl -p -i -e 's/All In One/Z33/gi' Lexmark-Z33-lxx74.ppd
cp lxx74.ppd Lexmark-Z24-lxx74.ppd
perl -p -i -e 's/All In One/Z24/gi' Lexmark-Z24-lxx74.ppd
cp lxx74.ppd Lexmark-Z34-lxx74.ppd
perl -p -i -e 's/All In One/Z34/gi' Lexmark-Z34-lxx74.ppd
cp lxx74.ppd Lexmark-Z25-lxx74.ppd
perl -p -i -e 's/All In One/Z25/gi' Lexmark-Z25-lxx74.ppd
cp lxx74.ppd Lexmark-Z35-lxx74.ppd
perl -p -i -e 's/All In One/Z35/gi' Lexmark-Z35-lxx74.ppd
cp lxx74.ppd Lexmark-Inkjet_Printer-lxx74.ppd
perl -p -i -e 's/All In One/Inkjet Printer/gi' Lexmark-Inkjet_Printer-lxx74.ppd
cp lxx74.ppd Lexmark-InkJet_4104-lxx74.ppd
perl -p -i -e 's/All In One/Inkjet 4104/gi' Lexmark-Inkjet_4104-lxx74.ppd
cp lxx74.ppd Samsung-MJC-940-lxx74.ppd
perl -p -i -e 's/All In One/MJC-940/gi' Samsung-MJC-940-lxx74.ppd
cp lxx74.ppd Samsung-MJC-950-lxx74.ppd
perl -p -i -e 's/All In One/MJC-950/gi' Samsung-MJC-950-lxx74.ppd
cp lxx74.ppd Samsung-MJC-2200-lxx74.ppd
perl -p -i -e 's/All In One/MJC-2200/gi' Samsung-MJC-2200-lxx74.ppd
cp lxx74.ppd Samsung-MJC-2130-lxx74.ppd
perl -p -i -e 's/All In One/MJC-2130/gi' Samsung-MJC-2130-lxx74.ppd
cp lxx74.ppd Samsung-MJC-530-lxx74.ppd
perl -p -i -e 's/All In One/MJC-530/gi' Samsung-MJC-530-lxx74.ppd
perl -p -i -e 's/Lexmark/Samsung/gi' Samsung-*-lxx74.ppd
gzip -9 *.ppd

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/cups
install -d %{buildroot}%{_prefix}/lib/cups/filter
install -d %{buildroot}%{_datadir}/cups/data
install -d %{buildroot}%{_datadir}/cups/model/%{rname}

install -m0755 rasterto%{rname} %{buildroot}%{_prefix}/lib/cups/filter/rasterto%{rname}.bin
install -m0644 self-portrait.out.gz %{buildroot}%{_datadir}/cups/data/self-portrait.out.gz

cat << EOF > %{buildroot}%{_prefix}/lib/cups/filter/rasterto%{rname}
#!/bin/bash
export self_portrait="%{_datadir}/cups/data/self-portrait.out.gz"
exec %{_prefix}/lib/cups/filter/rasterto%{rname}.bin "\$@"
EOF
chmod 755 %{buildroot}%{_prefix}/lib/cups/filter/rasterto%{rname}

install -m0644 %{rname}.types %{buildroot}%{_sysconfdir}/cups/
install -m0644 %{rname}.convs %{buildroot}%{_sysconfdir}/cups/
install -m0644 *.ppd* %{buildroot}%{_datadir}/cups/model/%{rname}/

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cups/%{rname}.convs
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/cups/%{rname}.types
%attr(0755,root,root) %{_prefix}/lib/cups/filter/rasterto%{rname}.bin
%attr(0755,root,root) %{_prefix}/lib/cups/filter/rasterto%{rname}
%attr(0644,root,root) %{_datadir}/cups/data/self-portrait.out*
%attr(0755,root,root) %dir %{_datadir}/cups/model/%{rname}
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Compaq-IJ670-%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Compaq-Inkjet_Printer-%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Lexmark-InkJet_4104-%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Lexmark-Inkjet_Printer-%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Lexmark-X74-%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Lexmark-X75-%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Lexmark-X76-%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Lexmark-Z13-%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Lexmark-Z14-%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Lexmark-Z23-%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Lexmark-Z24-%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Lexmark-Z25-%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Lexmark-Z33-%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Lexmark-Z34-%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Lexmark-Z35-%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Samsung-MJC-2130-%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Samsung-MJC-2200-%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Samsung-MJC-530-%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Samsung-MJC-940-%{rname}.ppd*
%attr(0644,root,root) %{_datadir}/cups/model/%{rname}/Samsung-MJC-950-%{rname}.ppd*


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.8.4.2-10mdv2011.0
+ Revision: 663438
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.4.2-9mdv2011.0
+ Revision: 603870
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.4.2-8mdv2010.1
+ Revision: 518884
- fix deps
- rebuild

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.8.4.2-7mdv2010.0
+ Revision: 413286
- rebuild

* Tue Dec 23 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.4.2-6mdv2009.1
+ Revision: 318070
- use %%ldflags

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 0.8.4.2-5mdv2009.0
+ Revision: 220540
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 0.8.4.2-4mdv2008.1
+ Revision: 149147
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.4.2-3mdv2008.0
+ Revision: 75327
- fix deps (pixel)

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.4.2-2mdv2008.0
+ Revision: 64148
- use the new System/Printing RPM GROUP

* Mon Aug 13 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.4.2-1mdv2008.0
+ Revision: 62506
- Import cups-drivers-lxx74



* Mon Aug 13 2007 Oden Eriksson <oeriksson@mandriva.com> 0.8.4.2-1mdv2008.0
- initial Mandriva package

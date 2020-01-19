%global	fontname	smc

# Common description
%global common_desc \
The SMC Fonts package contains fonts for the display of\
traditional and new Malayalam Script.

Name:		%{fontname}-fonts
Version:	6.0
Release:	7%{?dist}
Summary:	Open Type Fonts for Malayalam script
License:	GPLv3+ with exceptions and GPLv2+ with exceptions and GPLv2+ and  GPLv2 and GPL+
URL:		http://savannah.nongnu.org/projects/smc
Source0:	http://download.savannah.gnu.org/releases-noredirect/smc/fonts/malayalam-fonts-%{version}.tar.xz
Source1: 65-0-smc-meera.conf
Source2: 67-smc-anjalioldlipi.conf
Source3: 67-smc-dyuthi.conf
Source4: 67-smc-kalyani.conf
Source5: 65-0-smc-rachana.conf
Source6: 67-smc-raghumalayalam.conf
Source7: 67-smc-suruma.conf
Source8: AnjaliOldLipi-license-confirmation-email.txt
BuildArch:	noarch
BuildRequires:	fontpackages-devel > 1.13
BuildRequires:	fontforge >= 20080429
# https://bugzilla.redhat.com/show_bug.cgi?id=803234
Patch1: bug-803234.patch

%description
%common_desc

%package common
Summary:  Common files for smc-fonts
Requires: fontpackages-filesystem

%description common
%common_desc

%package -n %{fontname}-dyuthi-fonts
Summary: Open Type Fonts for Malayalam script
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
%description -n %{fontname}-dyuthi-fonts
The Dyuthi font package contains fonts for the display of
traditional Malayalam Scripts.

%_font_pkg -n dyuthi -f 67-smc-dyuthi.conf Dyuthi*.ttf 
%doc Dyuthi/COPYING

%package -n %{fontname}-meera-fonts
Summary: Open Type Fonts for Malayalam script
Requires: %{name}-common = %{version}-%{release}
License: GPLv2+ with exceptions
%description -n %{fontname}-meera-fonts
The Meera font package contains fonts for the display of
traditional Malayalam Scripts.

%_font_pkg -n meera -f 65-0-smc-meera.conf Meera.ttf 
%doc Meera/COPYING Meera/README


%package -n %{fontname}-rachana-fonts
Summary: Open Type Fonts for Malayalam script
Requires: %{name}-common = %{version}-%{release}
License: GPLv2+
%description -n %{fontname}-rachana-fonts
The Rachana font package contains fonts for the display of
traditional Malayalam Scripts.

%_font_pkg -n rachana -f 65-0-smc-rachana.conf Rachana.ttf
%doc Rachana/COPYING Rachana/LICENSE Rachana/README


%package -n %{fontname}-raghumalayalam-fonts
Summary: Open Type Fonts for Malayalam script
Requires: %{name}-common = %{version}-%{release}
License: GPLv2
%description -n %{fontname}-raghumalayalam-fonts
The SMC Malayalam fonts package contains fonts for the display of
new Malayalam Scripts.

%_font_pkg -n raghumalayalam -f 67-smc-raghumalayalam.conf RaghuMalayalamSans.ttf
%doc RaghuMalayalamSans/COPYING

%package -n %{fontname}-suruma-fonts
Summary: Open Type Fonts for Malayalam script
Requires: %{name}-common = %{version}-%{release}
License: GPLv3 with exceptions
%description -n %{fontname}-suruma-fonts
The Suruma font package contains fonts for the display of
traditional Malayalam Scripts.

%_font_pkg -n suruma -f 67-smc-suruma.conf Suruma.ttf
%doc Suruma/COPYING Suruma/README

%package -n %{fontname}-kalyani-fonts
Summary: Open Type Fonts for Malayalam script
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
%description -n %{fontname}-kalyani-fonts
The Kalyani font package contains fonts for the display of
new Malayalam Scripts.

%_font_pkg -n kalyani -f 67-smc-kalyani.conf Kalyani.ttf
%doc Kalyani/COPYING

%package -n %{fontname}-anjalioldlipi-fonts
Summary: Open Type Fonts for Malayalam script
Requires: %{name}-common = %{version}-%{release}
License: GPL+
%description -n %{fontname}-anjalioldlipi-fonts
The Anjali OldLipi package contains fonts for the display of
traditional Malayalam Scripts.

%_font_pkg -n anjalioldlipi -f 67-smc-anjalioldlipi.conf AnjaliOldLipi.ttf
%doc AnjaliOldLipi/COPYING


%prep
%setup -q -n fonts
%patch1 -p1 -b .1-panose-setting
sed -i 's/\r//' */COPYING
sed -i 's/\r//' Rachana/LICENSE

%build
chmod +x generate.pe
make

%install
#%%{_fontdir} is shared by all subpackages since they all are for malayalam script only
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p AnjaliOldLipi/*.ttf %{buildroot}%{_fontdir}
install -m 0644 -p Dyuthi/*.ttf %{buildroot}%{_fontdir}
install -m 0644 -p Kalyani/*.ttf %{buildroot}%{_fontdir}
install -m 0644 -p Meera/*.ttf %{buildroot}%{_fontdir}
install -m 0644 -p Rachana/*.ttf %{buildroot}%{_fontdir}
install -m 0644 -p RaghuMalayalamSans/*.ttf %{buildroot}%{_fontdir}
install -m 0644 -p Suruma/*.ttf %{buildroot}%{_fontdir}
install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}
install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/65-0-smc-meera.conf
install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/67-smc-anjalioldlipi.conf
install -m 0644 -p %{SOURCE3} \
	%{buildroot}%{_fontconfig_templatedir}/67-smc-dyuthi.conf
install -m 0644 -p %{SOURCE4} \
	%{buildroot}%{_fontconfig_templatedir}/67-smc-kalyani.conf
install -m 0644 -p %{SOURCE5} \
	%{buildroot}%{_fontconfig_templatedir}/65-0-smc-rachana.conf
install -m 0644 -p %{SOURCE6} \
	%{buildroot}%{_fontconfig_templatedir}/67-smc-raghumalayalam.conf
install -m 0644 -p %{SOURCE7} \
	%{buildroot}%{_fontconfig_templatedir}/67-smc-suruma.conf

for fconf in 65-0-smc-meera.conf \
	     67-smc-anjalioldlipi.conf \
	     67-smc-dyuthi.conf \
	     67-smc-kalyani.conf \
	     65-0-smc-rachana.conf \
	     67-smc-raghumalayalam.conf \
	     67-smc-suruma.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
	%{buildroot}%{_fontconfig_confdir}/$fconf
done



%files common
%doc ChangeLog 

%changelog
* Thu Jan 23 2014 Pravin Satpute <psatpute@redhat.com> 6.0-7
- Resolves: rh#1056846: some packaging issues

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 6.0-6
- Mass rebuild 2013-12-27

* Tue Nov 19 2013 Pravin Satpute <psatpute@redhat.com> 6.0-1
- Resolves: rh#1023847 - Upstream new release with fix against Harfbuzz NG
- New release 6.0 with many new features and bug fixes
- v2 opentype spec support for Malayalam (mlm2) for Meera, Rachana, Raghumalayalam
- Full support to Harfbuzz, Adobe and Uniscribe shaping engines
- Cleaned up and updated lookup tables
- Meaningful names to glyphs to help with Lookup tables reusability
- Old Figures and other Typographical glyphs to Rachana
- Dotreph positioning using GPOS 'abvm' lookup
- Unicode 6.1 Malayalam glyphset for many fonts

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 27 2012 Pravin Satpute <psatpute@redhat.com> 5.0.1-4
- Spec file clean up #880052

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Apr 13 2012 Pravin Satpute <psatpute@redhat.com> 5.0.1-2
- Resolved bug 803234
- Updated panose for Meera, RaghuMalayalam and Kalyani
- Changed conf file of Rachana from Sans to Serir

* Sat Mar 17 2012 Rajeesh K Nambiar <rajeeshknambiar@gmail.com> 5.0.1-1
- New upstream release 5.0.1 introducing Unicode 5.1 compatibility
- Resolves Meera size issues
- Drop upstreamed patches for RHBZ# 545683, 616324 and 781938
- Resolves RHBZ# 803183
- Spec cleanup

* Mon Jan 16 2012 Pravin Satpute <psatpute@redhat.com> 4.4-7
- Resolved bug 781938

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 16 2010 Naveen Kumar <nkumar@redhat.com> - 4.4.4
- rectify error to directly install fonts in fontdir instead of subdir in fontdir
- Resolves bug #653608

* Tue Nov 16 2010 Rajeesh K Nambiar <rajeeshknambiar@gmail.com> - 4.4.3
- Resolves bug #653608

* Mon Aug 16 2010 Naveen Kumar <nkumar@redhat.com> - 4.4.2
- apply patch smc-fonts_616324.patch created from Pravin S' src Modification 
- resolves bug #616324

* Fri Jul 16 2010 Naveen Kumar <nkumar@redhat.com> - 4.4.1
- new release from upstream
- changes in spec file to incorporate new build from sfd source
- remove patch bug-523454.patch
- reolves bug #586283
- reolves bug #586286

* Fri Jun 11 2010 Naveen Kumar <nkumar@redhat.com> - 04.2.10
- resolves bug 563841

* Fri Apr 30 2010 Naveen Kumar <nkumar@redhat.com> - 04.2.9
- oops! forgot to rename 66-smc-meera.conf to 65-0-smc-meera.conf in INSTALL in spec file
- oops! forgot to remove 66-smc-meera.conf
- resolves Bug #586288

* Fri Apr 30 2010 Naveen Kumar <nkumar@redhat.com> - 04.2.8
- rename 66-smc-meera.conf  to 65-0-smc-meera.conf
- resolves Bug #586288

* Fri Apr 16 2010 Naveen Kumar <nkumar@redhat.com> - 04.2.7
- remove binding="same" from all .conf files
- resolves Bug #578046

* Thu Feb 25 2010 Pravin Satpute <psatpute@redhat.com> 04.2-6
- resolved bug 568229
- fixed license of suruma and anjali-old-lipi
- done .conf cleanup

* Tue Feb 23 2010 Pravin Satpute <psatpute@redhat.com> 04.2-5
- added .conf file for each subpackage
- fixed source url
- resolves bug : 567496

* Mon Dec 21 2009 Pravin Satpute <psatpute@redhat.com> 04.2-4
- updated meera conf file

* Wed Dec 09 2009 Pravin Satpute <psatpute@redhat.com> 04.2-3
- bugfix 545683

* Wed Oct 14 2009 Pravin Satpute <psatpute@redhat.com> 04.2-2
- bugfix 523454

* Tue Aug 18 2009 Rajeesh K Nambiar <rajeeshknambiar@gmail.com> 04.2-1
- bugfix 484536 for Meera

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 04.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 03 2009 Pravin Satpute <psatpute@redhat.com> 04.1-6
- bugfix 493814
- added 'Provides' field for packages

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 04.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 22 2009 Rajeesh K Nambiar <rajeeshknambiar@gmail.com> 04.1-4
- change descriptions
- fix bug in kalyani font's obsoleting version number
- move _font_pkg macros next to corresponding packages

* Sat Jan 17 2009 Rajeesh K Nambiar <rajeeshknambiar@gmail.com> 04.1-3
- update for new font guidelines

* Tue Jan 06 2009 Pravin Satpute <psatpute@redhat.com> 04.1-2
- bugfix 477458
- updated spec

* Tue Jul 29 2008 Pravin Satpute <psatpute@redhat.com> 04.1-1
- new upstream release
- fontconfig rule for size adjustment of Meera is added
- two new fonts kalyani and anjalioldlipi
- bugfix 448078

* Tue Apr 15 2008 Pravin Satpute <psatpute@redhat.com> 04-6
- corrected meera fonts description it is for traditional script

* Tue Apr 15 2008 Pravin Satpute <psatpute@redhat.com> 04-5
- removed -n {fontname}-fonts from all fields

* Mon Apr 14 2008 Pravin Satpute <psatpute@redhat.com> 04-4
- added comment about sharing directory in spec file
- fontdir will be 'smc' only instead of 'smc-fonts' earlier

* Wed Apr 9 2008 Pravin Satpute <psatpute@redhat.com> 04-3
- defattr now comes after files
- s/malayalam/Malayalam in description
- removed '-fonts' from fontdir variable value

* Fri Apr 4 2008 Pravin Satpute <psatpute@redhat.com> 04-2
- done changes in spec file as suggested in review request
- changed variable name from xfontdir to fontdir
 
* Thu Apr 3 2008 Pravin Satpute <psatpute@redhat.com> 04-1 
- initial packaging

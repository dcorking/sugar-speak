%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

Name:           sugar-speak
Version:        28
Release:        1%{?dist}
Summary:        Speak for Sugar

Group:          Sugar/Activities
License:        GPLv2+ and GPLv3+
URL:            http://wiki.laptop.org/go/Speak
Source0:        http://download.sugarlabs.org/activities/4038/speak-%{version}.xo
BuildArch:      noarch

BuildRequires:  python
BuildRequires:  gettext
BuildRequires:  sugar-toolkit
Requires:       sugar
Requires:       numpy
Requires:       espeak

%description
Speak is a talking face for the XO laptop. Anything you type will be spoken
aloud using the XO's speech synthesizer, espeak. You can adjust the accent,
rate and pitch of the voice as well as the shape of the eyes and mouth. This
is a great way to experiment with the speech synthesizer, learn to type or 
just have fun making a funny face for your XO.  

%prep
%setup -q -n Speak.activity
rm -rf .0sugar bot

%build
%{__python} setup.py build

%install
%{__python} setup.py install --prefix=%{buildroot}%{_prefix}
find  %{buildroot}%{sugaractivitydir}Speak.activity/activity.py  -type f -name \* -exec chmod 644 {} \;
%find_lang vu.lux.olpc.Speak

%files -f vu.lux.olpc.Speak.lang
%defattr(-,root,root,-)
%doc NEWS COPYING
%{sugaractivitydir}/Speak.activity/

%changelog
* Wed Jul 13 2011 Peter Robinson <pbrobinson@gmail.com> - 28-1
- New 28 release

* Sat Jun 18 2011 Peter Robinson <pbrobinson@gmail.com> - 27-1
- New 27 release

* Mon Jun 13 2011 Peter Robinson <pbrobinson@gmail.com> - 26-1
- New 26 release

* Sat May  7 2011 Peter Robinson <pbrobinson@gmail.com> - 25-1
- New 25 release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 29 2011 Peter Robinson <pbrobinson@gmail.com> - 20-1
- New 20 release

* Mon Sep 06 2010 Fabian Affolter <fabian@bernewireless.net> - 14-6
- Fix install section to resolve #623386

* Wed Aug 11 2010 David Malcolm <dmalcolm@redhat.com> - 14-5
- recompiling .py files against Python 2.7 (rhbz#623386)

* Mon Mar 15 2010 Fabian Affolter <fabian@bernewireless.net> - 14-4
- Minor layout changes

* Tue Mar 09 2010 Sebastian Dziallas <sebastian@when.com> - 14-3
- Grab locales properly

* Tue Mar 09 2010 Sebastian Dziallas <sebastian@when.com> - 14-2
- Add gettext dependency

* Tue Mar 09 2010 Sebastian Dziallas <sebastian@when.com> - 14-1
- New upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 14 2008 Fabian Affolter <fabian@bernewireless.net> - 9-3
- Fixed add numpy and espeak to Requires

* Wed Nov 19 2008 Fabian Affolter <fabian@bernewireless.net> - 9-2
- Fixed license to GPLv3+

* Sun Oct 19 2008 Fabian Affolter <fabian@bernewireless.net> - 9-1
- Initial package for Fedora

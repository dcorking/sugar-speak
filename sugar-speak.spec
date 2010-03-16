Name:           sugar-speak
Version:        14
Release:        4%{?dist}
Summary:        Speak for Sugar

Group:          Sugar/Activities
License:        GPLv2+ and GPLv3+
URL:            http://wiki.laptop.org/go/Speak
Source0:        http://activities.sugarlabs.org/sugar/downloads/file/26826/speak-%{version}.xo
Patch0:         sugar-speak-no-aiml.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{_id_u} -n)
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
%patch0 -p1
# remove stuff we don't want
rm -rf .0sugar bot


%build
%{__python} setup.py build


%install
rm -rf  %{buildroot}
%{__python} install --prefix=%{buildroot}/%{_prefix}
find  %{buildroot}%{sugaractivitydir}Speak.activity/activity.py  -type f -name \* -exec chmod 644 {} \;
%find_lang vu.lux.olpc.Speak


%clean
rm -rf  %{buildroot}


%files -f vu.lux.olpc.Speak.lang
%defattr(-,root,root,-)
%doc NEWS COPYING
%{sugaractivitydir}/Speak.activity/


%changelog
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

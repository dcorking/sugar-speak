Name:           sugar-speak
Version:        9
Release:        5%{?dist}
Summary:        Speak for Sugar

Group:          Sugar/Activities
License:        GPLv3+
URL:            http://wiki.laptop.org/go/Speak
Source0:        Speak-%{version}.tar.bz2
Source1:        sugar-speak-checkout.sh
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{_id_u} -n)
BuildArch:      noarch

BuildRequires:  python
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
%setup -q -n Speak-%{version}/Speak.activity


%build
python ./setup.py build


%install
rm -rf  %{buildroot}
./setup.py install --prefix=%{buildroot}/%{_prefix}
find  %{buildroot}%{sugaractivitydir}Speak.activity/activity.py  -type f -name \* -exec chmod 644 {} \;


%clean
rm -rf  %{buildroot}


%files
%defattr(-,root,root,-)
%doc NEWS COPYING
%{sugaractivitydir}/Speak.activity/


%changelog
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

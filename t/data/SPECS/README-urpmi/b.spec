Summary: b
Name: b
Version: 1
Release: 1
License: x
Group: x
Url: x
BuildRoot: %{_tmppath}/%{name}

%description
x

%prep
rm -rf *
echo "installing %name" > README.install.urpmi
echo "upgrading %name" > README.upgrade.urpmi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.*

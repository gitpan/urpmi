Summary: x
Name: a
Version: 1
Release: 1
License: x
Group: x
Url: x
BuildArch: noarch

%description
x

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/dir
echo a > $RPM_BUILD_ROOT/etc/foo
echo bar > $RPM_BUILD_ROOT/etc/bar
echo a > $RPM_BUILD_ROOT/etc/dir/a

%clean
rm -rf $RPM_BUILD_ROOT

%files
/etc/*

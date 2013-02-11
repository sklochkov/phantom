%define _builddir .
%define _sourcedir .
%define _specdir .
%define _rpmdir .

Name: phantom
Version: 0.14.0
Release: pre44.1%{dist}

Summary: I/O engine for yandex loadtesting environment
License: LGPL 2.1
Group: System Environment/Libraries
Distribution: Red Hat Enterprise Linux

BuildArch: x86_64

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gcc-c++
BuildRequires: openssl-devel
BuildRequires: binutils-devel

%description
I/O engine for yandex loadtesting environment

%prep


%build
make -j $[`fgrep -c processor /proc/cpuinfo` + 1] -R all

%install
%{__rm} -rf %{buildroot}

#%{__make} -C src DESTDIR=%{buildroot} install
install -d -m755 %{buildroot}/usr/bin
install -d -m755 %{buildroot}/usr/lib64/phantom

install -m755 bin/phantom %{buildroot}/usr/bin/phantom
install -m755 lib/phantom/*.so %{buildroot}/usr/lib64/phantom/

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! -e /usr/lib/phantom ] ; then
	ln -sf /usr/lib64/phantom/ /usr/lib/
fi

%preun
rm -f /usr/lib/phantom

%files
%defattr(-,root,root)
%dir %attr(0755,root,root) /usr/lib64/phantom
%attr(0755,root,root) /usr/bin/phantom
%attr(0755,root,root) /usr/lib64/phantom/*


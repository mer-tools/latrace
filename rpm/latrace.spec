%define jobs 1

Name:       latrace
Summary:    LD_AUDIT feature frontend for glibc 2.4+
Version:    0
Release:    1
Group:      Development/Debuggers
License:    GPLv3+
URL:        http://people.redhat.com/jolsa/latrace
Source0:    http://people.redhat.com/jolsa/latrace/dl/%{name}-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  binutils-devel
BuildRequires:  flex

%description
allows you to trace library calls and get their statistics in a
manner similar to the strace utility (syscall tracing)

%prep
%setup -q -n %{name}-%{version}

%build
autoconf

%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

chmod 0755 %{buildroot}/%{_libdir}/libltaudit.so.*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc README ReleaseNotes TODO COPYING
%config(noreplace)  %{_sysconfdir}/*
%{_libdir}/libltaudit.so.*
%{_bindir}/latrace
%{_bindir}/latrace-ctl
# since we disabled asciidoc/xmlto, we appear to have disabled the manpages
# %{_mandir}/man1/*

%{?scl:%scl_package perl-IO-Socket-IP}

# Run optional test
%if ! (0%{?rhel}) && ! (0%{?scl:1})
%bcond_without perl_IO_Socket_IP_enables_optional_test
%else
%bcond_with perl_IO_Socket_IP_enables_optional_test
%endif

Name:           %{?scl_prefix}perl-IO-Socket-IP
Version:        0.39
Release:        451%{?dist}
Summary:        Drop-in replacement for IO::Socket::INET supporting both IPv4 and IPv6
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/IO-Socket-IP
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/IO-Socket-IP-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
# Runtime
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Errno)
BuildRequires:  %{?scl_prefix}perl(IO::Socket)
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(Socket) >= 1.97
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Tests only
BuildRequires:  %{?scl_prefix}perl(IO::Socket::INET)
BuildRequires:  %{?scl_prefix}perl(Test::More)
%if %{with perl_IO_Socket_IP_enables_optional_test} && !%{defined perl_bootstrap}
# Optional tests only
BuildRequires:  %{?scl_prefix}perl(Socket6)
BuildRequires:  %{?scl_prefix}perl(Test::Pod) >= 1.00
%endif
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))

%{?perl_default_filter}

%description
This module provides a protocol-independent way to use IPv4 and IPv6
sockets, as a drop-in replacement for IO::Socket::INET. Most constructor
arguments and methods are provided in a backward-compatible way.

%prep
%setup -q -n IO-Socket-IP-%{version}
chmod -x lib/IO/Socket/IP.pm

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
# Don't do the live test
rm -f t/21nonblocking-connect-internet.t
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
%doc Changes examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Fri Dec 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-451
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-439
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-438
- Increase release to favour standalone package

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-419
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-417
- Perl 5.28 re-rebuild of bootstrapped packages

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-416
- Increase release to favour standalone package

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.39-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-3
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-2
- Perl 5.26 rebuild

* Tue Mar 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.39-1
- 0.39 bump

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 09 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.38-1
- 0.38 bump

* Tue Jul 12 2016 Petr Pisar <ppisar@redhat.com> - 0.37-367
- Migrate from Module::Build to ExtUtils::MakeMaker
- Correct IO/Socket/IP.pm file mode

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-366
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.37-348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.37-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-345
- Increase release to favour standalone package

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.37-2
- Perl 5.22 rebuild

* Fri Mar 13 2015 Petr Šabata <contyk@redhat.com> - 0.37-1
- 0.37 bump

* Fri Jan 30 2015 Petr Šabata <contyk@redhat.com> - 0.36-1
- 0.36 bump
- Win32 changes only

* Mon Jan 05 2015 Petr Šabata <contyk@redhat.com> - 0.35-1
- 0.35 bugfix bump

* Fri Dec 12 2014 Petr Pisar <ppisar@redhat.com> - 0.34-2
- Do not build-require non-core Socket6 module when bootstrapping this core
  module

* Fri Dec 05 2014 Petr Šabata <contyk@redhat.com> - 0.34-1
- 0.34 bump, VMS bugfixes

* Tue Nov 25 2014 Petr Šabata <contyk@redhat.com> - 0.33-1
- 0.33 bump

* Thu Sep 18 2014 Petr Šabata <contyk@redhat.com> - 0.32-1
- 0.32 bump, implement connect timeout

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.31-2
- Perl 5.20 rebuild

* Wed Jul 16 2014 Petr Šabata <contyk@redhat.com> - 0.31-1
- 0.31 bump

* Wed Jul 09 2014 Petr Pisar <ppisar@redhat.com> - 0.30-2
- Fix multihomed SSL (bug #1116600)

* Mon Jul 07 2014 Petr Pisar <ppisar@redhat.com> - 0.30-1
- 0.30 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 26 2014 Petr Šabata <contyk@redhat.com> - 0.29-1
- 0.29 bump

* Wed Feb 12 2014 Petr Šabata <contyk@redhat.com> - 0.28-1
- 0.28 bump

* Tue Jan 21 2014 Petr Šabata <contyk@redhat.com> - 0.27-1
- 0.27 bump, test suite enhancements only

* Fri Jan 17 2014 Petr Šabata <contyk@redhat.com> - 0.26-1
- 0.26 bump

* Fri Sep 20 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.24-1
- 0.24 bump

* Mon Sep 16 2013 Petr Šabata <contyk@redhat.com> - 0.23-1
- 0.23 bump; smarter SO_REUSEPORT tests

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 31 2013 Petr Šabata <contyk@redhat.com> - 0.22-1
- 0.22 bump
- Test suite bugfix release

* Thu Jul 18 2013 Petr Šabata <contyk@redhat.com> - 0.21-3
- Disable the SO_REUSEPORT test; koji builders don't support this feature yet

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.21-2
- Perl 5.18 rebuild

* Mon Apr 29 2013 Petr Šabata <contyk@redhat.com> - 0.21-1
- 0.21 bump

* Wed Apr 17 2013 Petr Šabata <contyk@redhat.com> - 0.20-1
- 0.20 bump

* Tue Mar 12 2013 Petr Šabata <contyk@redhat.com> - 0.19-1
- 0.19 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 30 2012 Petr Šabata <contyk@redhat.com> - 0.18-1
- 0.18 bump

* Thu Nov 15 2012 Petr Šabata <contyk@redhat.com> - 0.17-2
- Fix a typo, sort the deps

* Wed Aug 22 2012 Petr Šabata <contyk@redhat.com> - 0.17-1
- 0.17 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 28 2012 Petr Pisar <ppisar@redhat.com> - 0.16-2
- Perl 5.16 rebuild

* Mon Jun 25 2012 Petr Šabata <contyk@redhat.com> - 0.16-1
- 0.16 (IO::Socket::INET compatibility enhancement)

* Thu Jun 21 2012 Petr Šabata <contyk@redhat.com> - 0.15-1
- 0.15 bump

* Tue Jun 19 2012 Petr Šabata <contyk@redhat.com> - 0.14-1
- 0.14 bump

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.11-2
- Perl 5.16 rebuild

* Wed Jun 06 2012 Petr Šabata <contyk@redhat.com> - 0.11-1
- 0.11 bump

* Fri May 11 2012 Petr Šabata <contyk@redhat.com> - 0.10-1
- 0.10 bump

* Wed Mar 14 2012 Petr Šabata <contyk@redhat.com> - 0.09-1
- 0.09 bump

* Fri Jan 27 2012 Petr Šabata <contyk@redhat.com> 0.08-1
- Specfile autogenerated by cpanspec 1.78.

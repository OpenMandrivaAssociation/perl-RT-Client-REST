%define upstream_name    RT-Client-REST
%define upstream_version 0.44

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Talk to RT using REST protocol
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/RT/RT-Client-REST-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Encode)
BuildRequires:	perl(Error)
BuildRequires:	perl(Exception::Class)
BuildRequires:	perl(HTTP::Cookies)
BuildRequires:	perl(HTTP::Request::Common)
BuildRequires:	perl(LWP)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Test::Exception)
BuildArch:	noarch

%description
*RT::Client::REST* is */usr/bin/rt* converted to a Perl module. I needed to
implement some RT interactions from my application, but did not feel that
invoking a shell command is appropriate. Thus, I took *rt* tool, written by
Abhijit Menon-Sen, and converted it to an object-oriented Perl module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml CHANGES README
%{_mandir}/man3/*
%{perl_vendorlib}/RT/

%changelog
* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.410.0-1mdv2011.0
+ Revision: 552625
- update to 0.41

* Fri Apr 30 2010 Michael Scherer <misc@mandriva.org> 0.400.0-1mdv2010.1
+ Revision: 541122
- import perl-RT-Client-REST


* Fri Apr 30 2010 cpan2dist 0.4-1mdv
- initial mdv release, generated with cpan2dist



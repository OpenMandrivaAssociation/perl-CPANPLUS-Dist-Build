%define	modname	CPANPLUS-Dist-Build
%define modver	0.68

Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	3
License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Constants for CPANPLUS::Dist::Build
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/%{modname}-%{modver}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(CPANPLUS)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IPC::Cmd)
BuildRequires:	perl(Locale::Maketext::Simple)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Module::Load)
BuildRequires:	perl(Module::Load::Conditional)
BuildRequires:	perl(Module::Pluggable)
BuildRequires:	perl(Object::Accessor)
BuildRequires:	perl(Params::Check)
BuildRequires:	perl(Test::Harness)
BuildRequires:	perl(Test::More)
# versionning the corresponding virtual package is not enough
BuildRequires:	perl-Module-Load-Conditional
BuildArch:	noarch

%description
'CPANPLUS::Dist::Build' is a distribution class for 'Module::Build' related
modules. Using this package, you can create, install and uninstall perl
modules. It inherits from 'CPANPLUS::Dist'.

Normal users won't have to worry about the interface to this module, as it
functions transparently as a plug-in to 'CPANPLUS' and will just 'Do The
Right Thing' when it's loaded.

%prep
%setup -q -n %{modname}-%{modver} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/CPANPLUS

%changelog
* Sat Dec 29 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.680.0-1
- cleanups
- new version

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.560.0-4mdv2012.0
+ Revision: 765117
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.560.0-3
+ Revision: 763574
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 0.560.0-2
+ Revision: 763235
- force it
- rebuild

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.560.0-1
+ Revision: 659893
- update to new version 0.56

* Wed Mar 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.540.0-1
+ Revision: 641332
- update to new version 0.54

* Sat Jan 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.520.0-1mdv2011.0
+ Revision: 630619
- update to new version 0.52

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.500.0-1mdv2011.0
+ Revision: 595090
- update to new version 0.50

* Sun Jan 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.460.0-1mdv2011.0
+ Revision: 495427
- update to 0.46

* Thu Nov 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.440.0-1mdv2010.1
+ Revision: 467356
- update to 0.44

* Mon Nov 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.420.0-1mdv2010.1
+ Revision: 466432
- update to 0.42

* Mon Sep 07 2009 Jérôme Quelin <jquelin@mandriva.org> 0.400.0-1mdv2010.0
+ Revision: 432797
- update to 0.40

* Tue Aug 25 2009 Jérôme Quelin <jquelin@mandriva.org> 0.380.0-1mdv2010.0
+ Revision: 420892
- update to 0.38

* Thu Jul 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.360.0-1mdv2010.0
+ Revision: 393728
- new version

* Tue Jun 02 2009 Jérôme Quelin <jquelin@mandriva.org> 0.320.0-1mdv2010.0
+ Revision: 382237
- update to 0.32
- using %%perl_convert_version
- fixed license field

* Tue May 19 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30-1mdv2010.0
+ Revision: 377483
- update to new version 0.30

* Sat May 16 2009 Jérôme Quelin <jquelin@mandriva.org> 0.28-1mdv2010.0
+ Revision: 376346
- update to new version 0.28

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.24-2mdv2010.0
+ Revision: 376052
- skipping tests that should be working
- rebuild
- import perl-CPANPLUS-Dist-Build


* Wed May 06 2009 cpan2dist 0.24-1mdv
- initial mdv release, generated with cpan2dist


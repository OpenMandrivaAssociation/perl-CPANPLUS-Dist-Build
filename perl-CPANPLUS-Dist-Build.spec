%define	modname	CPANPLUS-Dist-Build
Summary:	Constants for CPANPLUS::Dist::Build
Name:		perl-%{modname}
Version:	0.68
Release:	14
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/B/BI/BINGOS/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
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

%description
'CPANPLUS::Dist::Build' is a distribution class for 'Module::Build' related
modules. Using this package, you can create, install and uninstall perl
modules. It inherits from 'CPANPLUS::Dist'.

Normal users won't have to worry about the interface to this module, as it
functions transparently as a plug-in to 'CPANPLUS' and will just 'Do The
Right Thing' when it's loaded.

%prep
%setup -qn %{modname}-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE
%{perl_vendorlib}/CPANPLUS
%{_mandir}/man3/*


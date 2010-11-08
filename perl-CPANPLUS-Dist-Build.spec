%define upstream_name       CPANPLUS-Dist-Build
%define upstream_version 0.50

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Constants for CPANPLUS::Dist::Build
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl-devel
BuildRequires: perl(CPANPLUS)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IPC::Cmd)
BuildRequires: perl(Locale::Maketext::Simple)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Module::Load)
BuildRequires: perl(Module::Load::Conditional)
BuildRequires: perl(Module::Pluggable)
BuildRequires: perl(Object::Accessor)
BuildRequires: perl(Params::Check)
BuildRequires: perl(Test::Harness)
BuildRequires: perl(Test::More)
# versionning the corresponding virtual package is not enough
BuildRequires: perl-Module-Load-Conditional
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
'CPANPLUS::Dist::Build' is a distribution class for 'Module::Build' related
modules. Using this package, you can create, install and uninstall perl
modules. It inherits from 'CPANPLUS::Dist'.

Normal users won't have to worry about the interface to this module, as it
functions transparently as a plug-in to 'CPANPLUS' and will just 'Do The
Right Thing' when it's loaded.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/CPANPLUS

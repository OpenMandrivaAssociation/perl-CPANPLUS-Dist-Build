
%define realname   CPANPLUS-Dist-Build
%define version    0.24
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Constants for CPANPLUS::Dist::Build
Source:     http://www.cpan.org/modules/by-module/CPANPLUS/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
BuildRequires: perl(Params::Check)
BuildRequires: perl(Test::Harness)
BuildRequires: perl(Test::More)

BuildArch: noarch

%description
'CPANPLUS::Dist::Build' is a distribution class for 'Module::Build' related
modules. Using this package, you can create, install and uninstall perl
modules. It inherits from 'CPANPLUS::Dist'.

Normal users won't have to worry about the interface to this module, as it
functions transparently as a plug-in to 'CPANPLUS' and will just 'Do The
Right Thing' when it's loaded.



%prep
%setup -q -n %{realname}-%{version} 

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
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*



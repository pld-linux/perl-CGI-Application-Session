#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	Application-Session
Summary:	Plugin that adds session support to CGI::Application
Summary(pl):	Wtyczka dodaj±ca obs³ugê sesji do CGI::Application
Name:		perl-CGI-Application-Session
Version:	0.03
Release:	1
# Same as Perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ab8e45598fedab3710ee2c10aa0fff04
%if %{with tests}
BuildRequires:	perl-CGI-Application >= 3.21
BuildRequires:	perl-CGI-Session >= 3.95
#endif
BuildRequires:	perl-Module-Build >= 0.20
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Application::Session seamlessly adds session support to your
CGI::Application modules by providing a CGI::Session object that is
accessible from anywhere in the application.

%description -l pl
CGI::Application::Session dodaje obs³ugê sesji do modu³ów
CGI::Application poprzez dostarczenie obiektu CGI::Session dostêpnego
z dowolnego miejsca w aplikacji.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT

./Build
%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CGI/Application/*
%{_mandir}/man3/*

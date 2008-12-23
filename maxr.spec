#
# TODO:	- put config files to /etc
#	- do not create log files in . dir
#
Summary:	-
Summary(pl.UTF-8):	-
Name:		maxr
Version:	0.2.1
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.maxthegame.de/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	1281bf4ae0461b941382ba0f394e04bc
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-data.patch
URL:		http://www.maxthegame.de/
BuildRequires:	SDL_mixer-devel >= 1.2
BuildRequires:	SDL_net-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/{AUTHORS,COPYING,MANUAL}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ABOUT CHANGELOG data/{AUTHORS,MANUAL}
%attr(755,root,root) %{_bindir}/maxr
%{_datadir}/%{name}

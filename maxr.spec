#
# NOTE: source code contains some references to inexistent files, it means game is not playable in this stage
#
# TODO:	- put config files to /etc
#	- do not create log files in . dir
#
Summary:	Strategy game
Summary(pl.UTF-8):	Gra startegiczna
Name:		maxr
Version:	0.2.1
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games/Strategy
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
M.A.X.R. (Mechanized Assault and Exploration Reloaded) is a fanproject
by the community of MaxTheGame.de. It was founded by MM (Michael
Mönch) around 2006 and became OpenSource at the end of 2007. MAXR is
based on the old M.A.X.(Mechanized Assault and Exploration) by
Interplay from 1996.

%description -l pl.UTF-8
M.A.X.R. (Mechanized Assault and Exploration Reloaded) jest projektem
fanów społeczność MaxTheGame.de. Została ona założona przez MM
(Michaela Möncha) około roku 2006 i stała się ona wolnym projektem
pod koniec roku 2007. MAXR bazuje na starej grze M.A.X. (Mechanized
Assault and Exploration) stworzonej przez Interplay w 1996 roku.

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

# remove usless stuff (packaged in docs)
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/{AUTHORS,COPYING,MANUAL}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ABOUT CHANGELOG data/{AUTHORS,MANUAL}
%attr(755,root,root) %{_bindir}/maxr
%{_datadir}/%{name}

Summary:	XMMS plugin for playing Vortex format AY/YM music
Summary(pl):	Wtyczka wej¶ciowa dla XMMS-a odtwarzaj±ca pliki muzyczne AY/YM w formacie Vortex
Name:		xmms-input-vtx
Version:	0.8.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/libayemu/xmms-vtx-%{version}.tar.gz
# Source0-md5:	c7db5d5093df31809cf5d9d838d1a78b
Patch0:		%{name}-ac.patch
URL:		http://sashnov.nm.ru/libayemu.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libayemu-devel >= 0.9
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.0.0
Requires:	libayemu >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMMS plugin for playing AY/YM music in Vortex format. This format was
used on many 8-bit computers like ZX Spectrum, Amstrad, Atari.

%description -l pl
Wtyczka wej¶ciowa dla XMMS-a odtwarzaj±ca pliki muzyczne AY/YM w
formacie Vortex. Format ten by³ u¿ywany na wielu 8 bitowych
komputerach takich jak ZX Spectrum, Amstrad, Atari.

%prep
%setup -q -n xmms-vtx-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{xmms_input_plugindir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{xmms_input_plugindir}/*.so

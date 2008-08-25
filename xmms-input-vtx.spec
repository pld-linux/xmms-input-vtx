Summary:	XMMS plugin for playing Vortex format AY/YM music
Summary(pl.UTF-8):	Wtyczka wejściowa dla XMMS-a odtwarzająca pliki muzyczne AY/YM w formacie Vortex
Name:		xmms-input-vtx
Version:	0.9.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/libayemu/xmms-vtx-%{version}.tar.gz
# Source0-md5:	3d12ae042494250f7fe46c0b68d117c2
URL:		http://sashnov.nm.ru/libayemu.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel >= 1.2.3
BuildRequires:	libayemu-devel >= 0.9
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.0.0
Requires:	libayemu >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMMS plugin for playing AY/YM music in Vortex format. This format was
used on many old computers like ZX Spectrum, Amstrad, Atari ST.

%description -l pl.UTF-8
Wtyczka wejściowa dla XMMS-a odtwarzająca pliki muzyczne AY/YM w
formacie Vortex. Format ten był używany na wielu starych komputerach
takich jak ZX Spectrum, Amstrad, Atari ST.

%prep
%setup -q -n xmms-vtx-%{version}

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

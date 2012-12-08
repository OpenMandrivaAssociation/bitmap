Name:		bitmap
Version:	1.0.6
Release:	%mkrel 1
Summary:	Bitmap editor and converter utilities for the X Window System
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
URL:		http://xorg.freedesktop.org/archive/X11R6.8.0/doc/bitmap.1.html
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	libx11-devel >= 1.0.0
BuildRequires:	libxmu-devel >= 1.0.0
BuildRequires:	libxt-devel >= 1.0.0
BuildRequires:	libxaw-devel >= 1.0.1
BuildRequires:	x11-data-bitmaps >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1

%description
Bitmap provides is a bitmap editor and misc converter utilities for the X
Window System.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --disable-dependency-tracking
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/atobm
%{_bindir}/bmtoa
%{_bindir}/bitmap
%{_datadir}/X11/app-defaults/Bitmap
%{_datadir}/X11/app-defaults/Bitmap-nocase
%{_datadir}/X11/app-defaults/Bitmap-color
%{_includedir}/X11/bitmaps/Up
%{_includedir}/X11/bitmaps/Down
%{_includedir}/X11/bitmaps/Excl
%{_includedir}/X11/bitmaps/Fold
%{_includedir}/X11/bitmaps/Left
%{_includedir}/X11/bitmaps/Term
%{_includedir}/X11/bitmaps/Dashes
%{_includedir}/X11/bitmaps/Right
%{_includedir}/X11/bitmaps/FlipHoriz
%{_includedir}/X11/bitmaps/RotateLeft
%{_includedir}/X11/bitmaps/RotateRight
%{_includedir}/X11/bitmaps/FlipVert
%{_includedir}/X11/bitmaps/Stipple
%{_mandir}/man1/bitmap.1*
%{_mandir}/man1/bmtoa.1*
%{_mandir}/man1/atobm.1*





%changelog

* Fri Mar 09 2012 tv <tv> 1.0.6-1.mga2
+ Revision: 222329
- drop patch 0 (fixed otherwise upstream)
- new release

* Sun Jan 23 2011 pterjan <pterjan> 1.0.5-1.mga1
+ Revision: 35136
- Drop old scriptet
- imported package bitmap


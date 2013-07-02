Summary:	Editor and converter utilities for the X Window System
Name:		bitmap
Version:	1.0.7
Release:	2
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org/archive/X11R6.8.0/doc/bitmap.1.html
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xbitmaps)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xt)

%description
Bitmap provides is a bitmap editor and misc converter utilities for the X
Window System.

%prep
%setup -q

%build
%configure2_5x \
	--disable-dependency-tracking
%make

%install
%makeinstall_std

%files
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


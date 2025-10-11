%define appid   dev.geopjr.Tuba
Name:           tuba
Version:        0.10.3
Release:        1
Summary:        Browse the Fediverse - mastodon client
Group:          Internet
License:        GPL-3.0-only
URL:            https://github.com/GeopJr/Tuba
Source:         %{url}/archive/v%{version}/Tuba-%{version}.tar.gz
BuildRequires:  appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  pkgconfig(clapper-0.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libspelling-1)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  gstreamer1.0-plugins-good
BuildRequires:  pkgconfig(webkitgtk-6.0)

Requires: gstreamer1.0-plugins-base
Requires: gstreamer1.0-plugins-good
Requires: gstreamer1.0-plugins-bad
Requires: gstreamer1.0-plugins-ugly

%description
Explore the federated social web with Tuba for GNOME. Stay connected to your
favorite communities, family and friends with support for popular Fediverse
platforms like Mastodon, GoToSocial, Akkoma & more!

%prep
%autosetup -n Tuba-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{appid}

%files -f %{appid}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{appid}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appid}*.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/gtksourceview-5/language-specs/
%{_datadir}/gtksourceview-5/styles/
%{_mandir}/man1/dev.geopjr.Tuba.1.*

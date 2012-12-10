%define lua_version	5.1

Summary:        Network access library for the Lua programming language
Name:           lua-socket
Version:        2.0.2
Release:        %mkrel 4
License:        MIT
Group:          Development/Other
URL:            http://www.tecgraf.puc-rio.br/~diego/professional/luasocket/
Source0:        luasocket-%{version}.tar.gz
Patch0:		luasocket-2.0.2-cflags.patch
BuildRequires:	lua-devel
Requires:	lua
Obsoletes:	%{mklibname luasocket 2} < %{version}-%{release}
Obsoletes:	%{mklibname luasocket 2 -d} < %{version}-%{release}
BuildRoot:      %_tmppath/%{name}-%{version}

%description
LuaSocket is a Lua extension library that is composed by two parts: a
C layer that provides support for the TCP and UDP transport layers,
and a set of Lua modules that add support for the SMTP (sending
e-mails), HTTP (WWW access) and FTP (uploading and downloading files)
protocols.

%prep
%setup -q -n luasocket-%{version}
%patch0 -p1 -b .cflags

%build
export CFLAGS="%{optflags} -fPIC"
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std INSTALL_TOP_SHARE=%{buildroot}/%{_datadir}/lua/%{lua_version} INSTALL_TOP_LIB=%{buildroot}/%{_libdir}/lua/%{lua_version}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEW README doc/*
%{_libdir}/lua/%{lua_version}/mime/*.so
%{_libdir}/lua/%{lua_version}/socket/*.so
%{_datadir}/lua/5.1/*.lua
%{_datadir}/lua/5.1/socket/*.lua


%changelog
* Wed Dec 08 2010 Rémy Clouard <shikamaru@mandriva.org> 2.0.2-4mdv2011.0
+ Revision: 616183
- rebuild for the mass rebuild

* Wed Sep 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.2-3mdv2010.0
+ Revision: 448047
- bump release
- package renaming
- package renaming

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.0.2-2mdv2010.0
+ Revision: 429883
- rebuild

* Thu Aug 28 2008 Adam Williamson <awilliamson@mandriva.org> 2.0.2-1mdv2009.0
+ Revision: 277052
- package doc files properly with %%doc
- drop now unnecessary %%post and %%postun workarounds
- drop the manual installation, just pass appropriate vars to makeinstall
- rewrap description
- obsolete the insane old packaging of this as if it were a system library
- correct lua buildrequires and requires
- add new cflags.patch for just the allowing external CFLAGS bit
- drop old patch (lots of irrelevant stuff in it)
- update URL
- rebuild for new lua
- drop unnecessary defines
- new release 2.0.2

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request
    - import luasocket

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot



%define lua_version	5.1

Summary:        Network access library for the Lua programming language
Name:           lua-socket
Version:        2.0.2
Release:        %{mkrel 2}
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
